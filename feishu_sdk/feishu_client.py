#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from typing import List

from feishu_sdk.base_client import BaseClient
from feishu_sdk.card.card import CardMessage
from feishu_sdk.card.modules import DivModule
from feishu_sdk.card.objects import LarkMdObj
from feishu_sdk.feishu_response import FeishuResponse


class FeishuClient(BaseClient):
    """
    TODO: 参数校验
    """
    async def user_batch_get(self, open_ids: List = None, employ_ids: List = None) -> FeishuResponse:
        params = {"open_ids": open_ids} if open_ids else {'employ_ids': employ_ids}
        auth_headers = await self.auth_headers()
        return await self.api_call("/contact/v1/user/batch_get", params=params, headers=auth_headers)

    async def user_batch_get_id(self, emails: List = [], mobiles: List = []) -> FeishuResponse:
        params = {'emails': emails, "mobiles": mobiles}
        auth_headers = await self.auth_headers()
        return await self.api_call("/user/v1/batch_get_id", params=params, headers=auth_headers)

    async def user_search(self, query: str, page_size: int = 20, page_token: str = None) -> FeishuResponse:
        params = {"query": query, "page_size": page_size}
        if page_token:
            params['page_token'] = page_token
        auth_headers = await self.auth_headers()
        return await self.api_call("/search/v1/user", params=params, headers=auth_headers)

    async def chat_create(self,
                          name: str,
                          description: str = None,
                          owner_open_id: str = None,
                          owner_user_id: str = None,
                          open_ids: List = None,
                          user_ids: List = None,
                          i18n_names: dict = None,
                          only_owner_add: bool = False,
                          share_allowed: bool = True,
                          add_member_verify: bool = False,
                          only_owner_at_all: bool = False,
                          only_owner_edit: bool = False,
                          send_message_permission: str = "all",
                          join_message_visibility: str = "all",
                          leave_message_visibility: str = "owner",
                          group_email_enabled: bool = False,
                          send_group_email_permission: str = "tenant_member") -> FeishuResponse:
        json = {"name": name}
        if owner_open_id:
            json["owner_open_id"] = owner_open_id
        if owner_user_id:
            json["owner_user_id"] = owner_user_id
        if open_ids:
            json["open_ids"] = open_ids
        if user_ids:
            json["user_ids"] = user_ids
        auth_headers = await self.auth_headers()
        return await self.api_call("/chat/v4/create/", json=json, headers=auth_headers)

    async def chat_info(self, chat_id: str) -> FeishuResponse:
        params = {"chat_id": chat_id}
        auth_headers = await self.auth_headers()
        return await self.api_call("/chat/v4/info", params=params, headers=auth_headers)

    async def chat_update(self,
                          chat_id: str,
                          name: str = None,
                          description: str = None,
                          owner_open_id: str = None,
                          owner_user_id: str = None,
                          i18n_names: dict = None,
                          only_owner_add: bool = False,
                          share_allowed: bool = True,
                          add_member_verify: bool = False,
                          only_owner_at_all: bool = False,
                          only_owner_edit: bool = False,
                          send_message_permission: str = "all",
                          join_message_visibility: str = "all",
                          leave_message_visibility: str = "owner",
                          group_email_enabled: bool = False,
                          send_group_email_permission: str = "tenant_member"):
        json = {"chat_id": chat_id}
        if name:
            json["name"] = name
        if description:
            json["description"] = description
        if owner_open_id:
            json["owner_open_id"] = owner_open_id
        if owner_user_id:
            json["owner_user_id"] = owner_user_id
        auth_headers = await self.auth_headers()
        return await self.api_call("/chat/v4/update/", json=json, headers=auth_headers)

    async def chat_chatter_add(self, chat_id: str, open_ids: List = None, user_ids: List = None):
        json = {"chat_id": chat_id}
        if open_ids:
            json["open_ids"] = open_ids
        if user_ids:
            json["user_ids"] = user_ids
        auth_headers = await self.auth_headers()
        return await self.api_call("/chat/v4/chatter/add/", json=json, headers=auth_headers)

    async def chat_chatter_delete(self, chat_id: str, open_ids: List = None, user_ids: List = None):
        json = {"chat_id": chat_id}
        if open_ids:
            json["open_ids"] = open_ids
        if user_ids:
            json["user_ids"] = user_ids
        auth_headers = await self.auth_headers()
        return await self.api_call("/chat/v4/chatter/delete/", json=json, headers=auth_headers)

    async def chat_disband(self, chat_id: str):
        json = {"chat_id": chat_id}
        auth_headers = await self.auth_headers()
        return await self.api_call("/chat/v4/disband", json=json, headers=auth_headers)

    async def chat_list(self, page_size: int = 100, page_token: str = None):
        params = {"page_size": page_size}
        if page_token:
            params["page_token"] = page_token
        auth_headers = await self.auth_headers()
        return await self.api_call("/chat/v4/list", params=params, headers=auth_headers)

    async def bot_info(self):
        auth_headers = await self.auth_headers()
        return await self.api_call("/bot/v3/info/", params={}, headers=auth_headers)

    async def bot_add(self, chat_id: str):
        json = {"chat_id": chat_id}
        auth_headers = await self.auth_headers()
        return await self.api_call("/bot/v3/add/", json=json, headers=auth_headers)

    async def bot_remove(self, chat_id: str):
        json = {"chat_id": chat_id}
        auth_headers = await self.auth_headers()
        return await self.api_call("/bot/v3/remove/", json=json, headers=auth_headers)

    async def message_batch_send(self,
                                 msg_type: str,
                                 content: object,
                                 department_ids: List = None,
                                 open_ids: List = None,
                                 user_ids: List = None):
        json = {"msg_type": msg_type, "content": content}
        if department_ids:
            json["department_ids"] = department_ids
        if open_ids:
            json["open_ids"] = open_ids
        if user_ids:
            json["user_ids"] = user_ids
        auth_headers = await self.auth_headers()
        return await self.api_call("/message/v4/batch_send/", json=json, headers=auth_headers)

    async def message_text_send(self,
                                text: str,
                                open_id: str = None,
                                user_id: str = None,
                                email: str = None,
                                chat_id: str = None,
                                root_id: str = None):
        return await self.__message_send("text", {"text": text}, open_id, user_id, email, chat_id, root_id)

    async def message_image_send(self,
                                 image_key: str,
                                 open_id: str = None,
                                 user_id: str = None,
                                 email: str = None,
                                 chat_id: str = None,
                                 root_id: str = None):
        return await self.__message_send("image", {"image_key": image_key}, open_id, user_id, email, chat_id, root_id)

    async def message_post_send(self,
                                content: List,
                                title: str = None,
                                zh_cn: object = None,
                                ja_jp: object = None,
                                en_us: object = None,
                                open_id: str = None,
                                user_id: str = None,
                                email: str = None,
                                chat_id: str = None,
                                root_id: str = None):
        post = {"content": content}
        if title:
            post["title"] = title
        if zh_cn:
            post["zh_cn"] = zh_cn
        if ja_jp:
            post["ja_jp"] = ja_jp
        if en_us:
            post["en_us"] = en_us
        return await self.__message_send("post", post, open_id, user_id, email, chat_id, root_id)

    async def message_share_chat_send(self,
                                      share_open_chat_id: str,
                                      open_id: str = None,
                                      user_id: str = None,
                                      email: str = None,
                                      chat_id: str = None,
                                      root_id: str = None):
        return await self.__message_send("share_chat", {"share_open_chat_id": share_open_chat_id}, open_id, user_id, email,
                                         chat_id, root_id)

    async def message_md_send(self, md: str, open_id: str = None, chat_id: str = None, root_id: str = None):
        div_module = DivModule(text=LarkMdObj(content=md))
        card = CardMessage(elements=[div_module])
        return await self.message_interactive_send(card=card, open_id=open_id, chat_id=chat_id, root_id=root_id)

    async def message_interactive_send(self,
                                       card: CardMessage,
                                       update_multi: bool = False,
                                       open_id: str = None,
                                       user_id: str = None,
                                       email: str = None,
                                       chat_id: str = None,
                                       root_id: str = None):
        card_json = json.dumps(card, default=lambda o: o.__dict__)
        card_dict = json.loads(card_json)
        kwards = {"card": card_dict, "update_multi": update_multi}
        return await self.__message_send("interactive",
                                         open_id=open_id,
                                         user_id=user_id,
                                         email=email,
                                         chat_id=chat_id,
                                         root_id=root_id,
                                         kwards=kwards)

    async def __message_send(self,
                             msg_type: str,
                             content: object = None,
                             open_id: str = None,
                             user_id: str = None,
                             email: str = None,
                             chat_id: str = None,
                             root_id: str = None,
                             kwards: dict = {}):
        json = {"msg_type": msg_type}
        if content:
            json["content"] = content
        if open_id:
            json["open_id"] = open_id
        if user_id:
            json["user_id"] = user_id
        if email:
            json["email"] = email
        if chat_id:
            json["chat_id"] = chat_id
        if root_id:
            json["root_id"] = root_id
        if kwards:
            json.update(kwards)

        auth_headers = await self.auth_headers()
        return await self.api_call("/message/v4/send/", json=json, headers=auth_headers)

    async def message_recall(self, message_id: str):
        json = {"message_id": message_id}
        auth_headers = await self.auth_headers()
        return await self.api_call("/message/v4/recall/", json=json, headers=auth_headers)

    async def message_read_info(self, message_id: str):
        json = {"message_id": message_id}
        auth_headers = await self.auth_headers()
        return await self.api_call("/message/v4/read_info/", json=json, headers=auth_headers)
