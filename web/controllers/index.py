# -*- coding: utf-8 -*-
from flask import Blueprint, g
from common.libs.Helper import ops_render

"""
 仪表盘界面
"""
# 定义一个蓝图 实例变量 route_index，然后传进去一个__name__作为内置对应程序名称
route_index = Blueprint('index_page', __name__)


# 注册路由 通过/ 访问我们的路由 首页
@route_index.route("/")
def index():
    return ops_render("index/index.html")
