# feishu-sdk

## install
```sh
$ pip3 install feishu-py-sdk
```

## feishu-client
```python
from feishu_sdk import FeishuClient

fc = FeishuClient(app_id="xxx", app_secret="xxx")
```

## feishu-server
```python
from feishu_sdk import FeishuServer

class Server(FeishuServer):
    def __init__(self, config:dict):
        FeishuServer.__init__(config)
    
    def _message_callback_event_handler(self, event:dict):
        # handle message
```