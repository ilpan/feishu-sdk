#!/usr/bin/env python
# -*- coding: utf-8 -*-

SUCCESS_CODE = 0
ERROR_CODE = -1
ERROR_MSG = "error"
CODE, MSG, DATA = "code", "msg", "data"


class FeishuResponse:
    def __init__(self, code: int, msg: str, data: object = None):
        self._code = code
        self._msg = msg
        self._data = data

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, msg):
        self._msg = msg

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def __str__(self) -> str:
        return f"FeishuResponse[code={self.code} msg={self.msg} data={self.data}]"


def error(e: Exception):
    return FeishuResponse(ERROR_CODE, str(e), {})


def of(resp: dict) -> FeishuResponse:
    fr = FeishuResponse(resp.get(CODE, ERROR_CODE), resp.get(MSG, ERROR_MSG), {})
    if DATA in resp:
        fr.data = resp[DATA]
    else:
        for prop, value in resp.items():
            if prop != CODE and prop != MSG:
                fr.data[prop] = value
    return fr