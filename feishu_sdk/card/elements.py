#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Optional

from feishu_sdk.card.objects import ConfirmObj, OptionObj, TextObj, UrlObj


class Element:
    def __init__(self, tag):
        self.tag = tag


class ImgEle(Element):
    def __init__(self, img_key: str, alt: TextObj, preview: bool = True):
        super().__init__("img")
        self.img_key = img_key
        self.alt = alt
        self.preview = preview


class ButtonEle(Element):
    def __init__(self,
                 text: TextObj,
                 url: Optional[str] = None,
                 multi_url: Optional[UrlObj] = None,
                 type: str = "default",
                 value: dict = None,
                 confirm: Optional[ConfirmObj] = None):
        super().__init__("button")
        self.text = text
        self.url = url
        self.multi_url = multi_url
        self.type = type
        self.value = value
        self.confirm = confirm


class SelectMenuEle(Element):
    """
    Attributes:
        tag: “select_static” / “select_person”
    """
    def __init__(self,
                 tag: str,
                 placeholder: TextObj = None,
                 initial_option: str = None,
                 options: List[OptionObj] = None,
                 value: dict = None,
                 confirm: ConfirmObj = None):
        super().__init__(tag)
        self.placeholder = placeholder
        self.initial_option = initial_option
        self.options = options
        self.value = value
        self.confirm = confirm


class OverflowEle(Element):
    def __init__(self, options: List[OptionObj], value: dict = None, confirm: ConfirmObj = None):
        super().__init__("overflow")
        self.options = options
        self.value = value
        self.confirm = confirm


class DatePickerEle(Element):
    """
    Attributes:
        tag: “date_picker” / “picker_time” / “picker_datetime”
        initial_date: "YYYY-MM-DD"
        initial_time: "HH:mm"
        initial_datetime: "YYYY-MM-DD HH:mm"
    """
    def __init__(self,
                 tag,
                 initial_date: str = None,
                 initial_time: str = None,
                 initial_datetime: str = None,
                 placeholder: str = None,
                 value: dict = None,
                 confirm: ConfirmObj = None):
        super().__init__(tag)
        self.initial_date = initial_date
        self.initial_time = initial_time
        self.initial_datetime = initial_datetime
        self.placeholder = placeholder
        self.value = value
        self.confirm = confirm
