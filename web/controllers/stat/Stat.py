# -*- coding: utf-8 -*-
from flask import Blueprint
from common.libs.Helper import ops_render

route_stat = Blueprint('stat_page', __name__)


@route_stat.route("/index")
def index():
    return ops_render("stat/index.html")


@route_stat.route("/shop")
def shop():
    return ops_render("stat/shop.html")


@route_stat.route("/member")
def memebr():
    return ops_render("stat/member.html")


@route_stat.route("/share")
def share():
    return ops_render("stat/share.html")
