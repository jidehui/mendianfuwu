# -*- coding: utf-8 -*-
"""
 小程序的api 入口
"""
from flask import Blueprint

route_api = Blueprint('api_page', __name__)
from web.controllers.api.Member import *
from web.controllers.api.Shop import *
from web.controllers.api.Order import *
from web.controllers.api.My import *
from web.controllers.api.Cart import *
from web.controllers.api.Address import *


@route_api.route('/')
def index():
    return "mendianfuwu Api v1.0~"
