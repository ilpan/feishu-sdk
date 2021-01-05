#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Optional, Union

from feishu_sdk.card.elements import Element, ImgEle
from feishu_sdk.card.objects import FieldObj, TextObj


class Module:
    def __init__(self, tag):
        self.tag = tag


class DivModule(Module):
    def __init__(self, text: TextObj, fields: List[FieldObj] = None, extra: Optional[Element] = None):
        super().__init__("div")
        self.text = text
        self.fields = fields
        self.extra = extra


class HrModule(Module):
    def __init__(self):
        super().__init__("hr")


class ImgModule(Module):
    """
    Attributes:
        mode: “fit_horizontal”, “crop_center”
    """
    def __init__(self, img_key: str, alt: TextObj, title: TextObj = None, mode: str = None, preview: bool = True):
        super().__init__("img")
        self.img_key = img_key
        self.alt = alt
        self.title = title
        self.mode = mode
        self.preview = preview


class ActionModule(Module):
    """
    Attributes:
        layout: “bisected”, “trisection”, “flow”
    """
    def __init__(self, actions: List[Element], layout: str = None):
        super().__init__("action")
        self.actions = actions
        self.layout = layout


class NoteModule(Module):
    def __init__(self, elements: List[Union[TextObj, ImgEle]]):
        super().__init__("note")
        self.elements = elements
