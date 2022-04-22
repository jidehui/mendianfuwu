# -*- coding: utf-8 -*-
"""
本地环境
"""
SERVER_PORT = 8899
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = "ime_shop"

# 拦截器过滤
IGNORE_URLS = [
    "^/user/login",
    "^/api"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

# 表示展示每页分为N条记录
PAGE_SIZE = 50

# 默认页面显示为N条记录
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除",
}

# 小程序端配置
MINI_APP = {
    'appid': "wxa3b8aea2f63e25c6",
    'callback_url': '/api/order/callback'
}
""" MINI_APP:换成自己的
    'appkey': '',
    'paykey': '',
    'mch_id': '',
"""

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

APP = {
    'domain': 'http://192.168.220.137:8899'
}

PAY_STATUS_MAPPING = {
    "1": "已支付",
    "-8": "待支付",
    "0": "已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0": "订单关闭",
    "1": "支付成功",
    "-8": "待支付",
    "-7": "待发货",
    "-6": "待确认",
    "-5": "待评价"
}
