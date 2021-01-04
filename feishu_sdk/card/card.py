#!/usr/bin/env python
# -*- coding: utf-8 -*-

from feishu_sdk.card.modules import Module
from typing import List, Optional


class CardConfig:
    def __init__(self,
                 wide_screen_mode: bool = True,
                 enable_forward: bool = True):
        self.wide_screen_mode = wide_screen_mode
        self.enable_forward = enable_forward


class CardHeader:
    def __init__(self, title: str, template: Optional[str] = None):
        self.title = title
        self.template = template


class CardMessage:
    def __init__(self,
                 elements: List[Module],
                 config: Optional[CardConfig] = None,
                 header: Optional[CardHeader] = None):
        self.elements = elements
        self.config = config
        self.header = header
