# -*- coding: utf-8 -*-
from flask import Blueprint
from common.libs.Helper import ops_render

route_shop = Blueprint('shop_page', __name__)


@route_shop.route("/index")
def index():
    return ops_render("shop/index.html")


@route_shop.route("/info")
def info():
    return ops_render("shop/info.html")


@route_shop.route("/set")
def set():
    return ops_render("shop/set.html")


@route_shop.route("/cat")
def cat():
    return ops_render("shop/cat.html")


@route_shop.route("/cat-set")
def catSet():
    return ops_render("shop/cat_set.html")
