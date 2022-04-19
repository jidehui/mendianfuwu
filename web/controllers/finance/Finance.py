# -*- coding: utf-8 -*-
from flask import Blueprint
from common.libs.Helper import ops_render

# 定义一个蓝图 实例变量 route_user，然后传进去一个__name__作为内置对应程序名称
route_finance = Blueprint('finance_page', __name__)


# 注册路由 通过/ 访问我们的路由
@route_finance.route("/index")
def index():
    return ops_render("/finance/index.html")


# 注册路由 通过/ 访问我们的路由
@route_finance.route("/pay-info")
def payInfo():
    return ops_render("/finance/pay_info.html")


# 注册路由 通过/ 访问我们的路由
@route_finance.route("/account")
def account():
    return ops_render("/finance/account.html")
