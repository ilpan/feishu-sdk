#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def async_test(coro):
    def wrapper(*args, **kwargs):
        future = coro(*args, **kwargs)
        return asyncio.get_event_loop().run_until_complete(future)

    return wrapper
