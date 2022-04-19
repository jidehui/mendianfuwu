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
    "^/user/login"
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
