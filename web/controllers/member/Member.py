# -*- coding: utf-8 -*-
from flask import Blueprint
from common.libs.Helper import ops_render

# 定义一个蓝图 实例变量 route_member，然后传进去一个__name__作为内置对应程序名称
route_member = Blueprint('member_page', __name__)


# 注册路由 通过/ 访问我们的路由 首页
@route_member.route("/index")
def index():
    return ops_render("/member/index.html")


@route_member.route("/info")
def info():
    return ops_render("/member/info.html")


@route_member.route("/set")
def set():
    return ops_render("/member/set.html")


@route_member.route("/comment")
def comment():
    return ops_render("/member/comment.html")
