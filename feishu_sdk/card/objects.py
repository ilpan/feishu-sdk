#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional


class Obj:
    pass


class TextObj(Obj):
    def __init__(self, tag: str, content: str, lines: Optional[int] = None):
        self.tag = tag
        self.content = content
        self.lines = lines


class PlainTextObj(TextObj):
    def __init__(self, content: str, lines: Optional[int] = None):
        super().__init__("plain_text", content, lines=lines)


class LarkMdObj(TextObj):
    def __init__(self, content: str, lines: Optional[int] = None):
        super().__init__("lark_md", content, lines=lines)


class FieldObj(Obj):
    def __init__(self, is_shot: bool, text: TextObj):
        self.is_shot = is_shot
        self.text = text


class UrlObj(Obj):
    def __init__(self, url: str, android_url: str, ios_url: str, pc_url: str):
        self.url = url
        self.android_url = android_url
        self.ios_url = ios_url
        self.pc_url = pc_url


class OptionObj(Obj):
    """
    Optional Object for selectMenu or overflowMenu
    """
    def __init__(self,
                 value: str,
                 text: Optional[TextObj] = None,
                 url: Optional[str] = None,
                 multi_url: Optional[UrlObj] = None):
        self.value = value
        self.text = text
        self.url = url
        self.multi_url = multi_url


class ConfirmObj(Obj):
    def __init__(self, title: PlainTextObj, text: PlainTextObj):
        self.title = title
        self.text = text
