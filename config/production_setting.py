# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/food_db?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"

"""
APP = {
    'domain': 'https://shop.jidehui.com'
}
"""
APP = {
    'domain': 'http://192.168.220.137:8899'
}

RELEASE_VERSION = "20220422001"
