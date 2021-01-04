#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import sys
import logging

from aiohttp import web, web_app, web_request

log = logging.getLogger(__name__)


class FeishuServer:
    def __init__(self, config:dict):
        self.verification_token = config.get("verification_token", None)
        self.encrypt_key = config.get("encrypt_key", None)
        self.host = config.get("host", "0.0.0.0")
        self.port = config.get("port", "2333")
        if not self.verification_token:
            log.error("Verification Token must be provided in config")
            sys.exit(1)
        self._register_event_handlers()
        self._register_callback_event_handlers()
    
    def _register_event_handlers(self):
        self.event_handlers = {
            "url_verification": self._url_verification_handler,
            "event_callback": self._event_callback_handler,
        }

    def _register_callback_event_handlers(self):
        self.callback_event_handlers = {
            "message": self._message_callback_event_handler,
        }

    def _update_callback_event_handlers(self, callback_event_handlers:dict):
        if callback_event_handlers is None:
            log.error("event handlers can't be None")
            return
        if self.callback_event_handlers:
            self.callback_event_handlers.update(callback_event_handlers)
        else:
            self.callback_event_handlers = callback_event_handlers

    def _url_verification_handler(self, data:dict):
        challenge = data.get("challenge", "")
        resp = {"challenge": challenge}
        return resp
    
    def _event_callback_handler(self, data:dict):
        event = data.get("event", None)
        event_type = event.get("type", "") if event else ""
        log.info(f"receive callback event:{event_type}")
        callback_event_handler = self.callback_event_handlers.get(event_type)
        if not callback_event_handler:
            msg = f"invalid callback event type:{event_type}"
            log.error(msg)
            return {"msg": msg}
        return callback_event_handler(event) or {}
    
    def _message_callback_event_handler(self, event:dict):
        # override it if you need
        pass

    async def bot_handler(self, request:web_request.Request):
        # data = await request.post()   # form请求
        data = await request.json()
        log.info("received data: %s", pprint.pformat(data))
        token = data.get("token", "")
        if token != self.verification_token:
            log.error(f"verification token not match, token={token}")
            return web.json_response({"msg": "got invalid verification token"})
        event_type = data.get("type", "")
        event_handler = self.event_handlers.get(event_type, None)
        if not event_handler:
            msg = f"invalid event type:{event_type}"
            log.error(msg)
            return web.json_response({"msg": msg})
        return web.json_response(event_handler(data))
    
    async def make_app(self) -> web_app.Application:
        app = web.Application()
        app.add_routes([web.post("/bot", self.bot_handler)])
        return app
    
    def run(self):
        web.run_app(self.make_app(), host=self.host, port=self.port)
