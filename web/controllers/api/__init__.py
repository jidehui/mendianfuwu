# -*- coding: utf-8 -*-
"""
 小程序的api 入口
"""
from flask import Blueprint

route_api = Blueprint('api_page', __name__)


@route_api.route('/')
def index():
    return "mendianfuwu Api v1.0~"
