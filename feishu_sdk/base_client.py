#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiohttp
import logging

from aiohttp.client import ClientSession
from feishu_sdk import feishu_response

log = logging.getLogger(__name__)


class BaseClient:
    BASE_URL = "https://open.feishu.cn/open-apis"

    def __init__(self,
                 base_url: str = BASE_URL,
                 app_id: str = None,
                 app_secret: str = None):
        self.base_url = base_url
        self.app_id = app_id
        self.app_secret = app_secret

    async def auth_headers(self):
        access_token = await self.tenant_access_token_internal()
        return {
            "Authorization": f"Bearer {access_token}"
        } if access_token else None

    async def tenant_access_token_internal(self) -> str:
        """
        return tenant_access_token
        """
        tat_key = "tenant_access_token"
        params = {"app_id": self.app_id, "app_secret": self.app_secret}
        resp = await self.api_call("/auth/v3/tenant_access_token/internal/",
                                   params=params)
        return resp.data[tat_key] if tat_key in resp.data else None

    async def api_call(self,
                       api: str,
                       params: dict = None,
                       json: dict = None,
                       headers: dict = {}) -> feishu_response.FeishuResponse:
        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                resp_json = await self.fetch(session,
                                             self.__build_url(api),
                                             params=params,
                                             json=json)
                return feishu_response.of(resp_json)
            except Exception as e:
                log.exception("fetch feishu resp error")
                return feishu_response.error(e)

    @staticmethod
    async def fetch(session: ClientSession,
                    url: str,
                    params: dict = None,
                    json: dict = None):
        if params is not None:
            async with session.get(url, params=params) as resp:
                return await resp.json()
        if json is not None:
            async with session.post(url, json=json) as resp:
                return await resp.json()

    def __build_url(self, api: str):
        return self.base_url.rstrip('/') + '/' + api.lstrip('/')
