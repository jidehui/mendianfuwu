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
    'appkey': '',
    'paykey': '',
    'mch_id': '',
    'callback_url': '/api/order/callback'
}

APP = {
    'domain': 'http://192.168.220.137:8899'
}
