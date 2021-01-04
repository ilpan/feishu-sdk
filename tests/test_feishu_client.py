#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests import TEST_APP_ID, TEST_APP_SECRET, TEST_CHAT_ID, TEST_OPEN_ID
import unittest
from feishu_sdk import FeishuClient
from tests.helpers import async_test

class TestFeishuClient(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.fc = FeishuClient(app_id=TEST_APP_ID, app_secret=TEST_APP_SECRET)

    def tearDown(self):
        pass

    # @async_test
    # async def test_user_batch_get(self):
    #     data = await self.fc.user_batch_get(open_ids=[TEST_OPEN_ID])
    #     print(f"==> test_user_batch_get: {data}\n")
    
    # @async_test
    # async def test_user_batch_get_id(self):
        # data = await self.fc.user_batch_get_id(mobiles=['xx'])
        # print(f"==> test_user_batch_get_id: {data}\n")
    
    # @async_test
    # async def test_search_user(self):
    #     data = await self.fc.user_search("xxx")
    #     print(f"==> test_search_user: {data}\n")
    
    # @async_test
    # async def test_chat_create(self):
        # data = await self.fc.chat_create("hello chat", open_ids=[TEST_OPEN_ID])
        # print(f"==> test_chat_create: {data}\n")
    
    # @async_test
    # async def test_chat_info(self):
        # data = await self.fc.chat_info(TEST_CHAT_ID)
        # print(f"==> test_chat_info: {data}\n")

    # @async_test
    # async def test_chat_update(self):
        # data = await self.fc.chat_update(TEST_CHAT_ID, name="hello chat2", description="hello every one") #, owner_open_id=TEST_OPEN_ID)
        # print(f"==> test_chat_update: {data}\n")

    # @async_test
    # async def test_chat_list(self):
    #     data = await self.fc.chat_list()
    #     print(f"==> test_chat_list: {data}\n") 
    
    # @async_test
    # async def test_bot_info(self):
    #     data = await self.fc.bot_info()
    #     print(f"==> test_bot_info: {data}\n")
    
    # @async_test
    # async def test_message_batch_send(self):
        # data = await self.fc.message_batch_send("text", {"text": "hello text"}, open_ids=[TEST_OPEN_ID])
        # print(f"==> test_message_batch_send: {data}\n")

    @async_test
    async def test_message_md_send(self):
        data = await self.fc.message_md_send("**hello**", open_id=TEST_OPEN_ID)
        print(f"==> test_message_md_send: {data}\n")

if __name__ == "__main__":
    unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(TestFeishuClient("test_chat_update"))
    # unittest.TextTestRunner().run(suite)