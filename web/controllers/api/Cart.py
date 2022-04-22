# -*- coding: utf-8 -*-
from web.controllers.api import route_api
from flask import request, jsonify, g
from common.models.shop.Shop import Shop
from common.models.member.MemberCart import MemberCart
from common.libs.member.CartService import CartService
from common.libs.Helper import selectFilterObj, getDictFilterField
from common.libs.UrlManager import UrlManager
from application import app, db
import json


@route_api.route("/cart/index")
def cartIndex():
    resp = {'code': 200, 'msg': '添加购物车成功~', 'data': {}}
    member_info = g.member_info
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "获取失败，伪登录~~"
        return jsonify(resp)
    cart_list = MemberCart.query.filter_by(member_id=member_info.id).all()
    data_cart_list = []
    if cart_list:
        shop_ids = selectFilterObj(cart_list, "shop_id")
        shop_map = getDictFilterField(Shop, Shop.id, "id", shop_ids)
        for item in cart_list:
            tmp_shop_info = shop_map[item.shop_id]
            tmp_data = {
                "id": item.id,
                "number": item.quantity,
                "shop_id": item.shop_id,
                "name": tmp_shop_info.name,
                "price": str(tmp_shop_info.price),
                "pic_url": UrlManager.buildImageUrl(tmp_shop_info.main_image),
                "active": True
            }
            data_cart_list.append(tmp_data)

    resp['data']['list'] = data_cart_list
    return jsonify(resp)


@route_api.route("/cart/set", methods=["POST"])
def setCart():
    resp = {'code': 200, 'msg': '添加购物车成功~', 'data': {}}
    req = request.values
    shop_id = int(req['id']) if 'id' in req else 0
    number = int(req['number']) if 'number' in req else 0
    if shop_id < 1 or number < 1:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败-1~~"
        return jsonify(resp)

    member_info = g.member_info
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败-2~~"
        return jsonify(resp)

    shop_info = Shop.query.filter_by(id=shop_id).first()
    if not shop_info:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败-3~~"
        return jsonify(resp)

    if shop_info.stock < number:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败,库存不足~~"
        return jsonify(resp)

    ret = CartService.setItems(member_id=member_info.id, food_id=shop_info.id, number=number)
    if not ret:
        resp['code'] = -1
        resp['msg'] = "添加购物车失败-4~~"
        return jsonify(resp)
    return jsonify(resp)


@route_api.route("/cart/del", methods=["POST"])
def delCart():
    resp = {'code': 200, 'msg': '添加购物车成功~', 'data': {}}
    req = request.values
    params_goods = req['goods'] if 'goods' in req else None

    items = []
    if params_goods:
        items = json.loads(params_goods)
    if not items or len(items) < 1:
        return jsonify(resp)

    member_info = g.member_info
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "删除购物车失败-1~~"
        return jsonify(resp)

    ret = CartService.deleteItem(member_id=member_info.id, items=items)
    if not ret:
        resp['code'] = -1
        resp['msg'] = "删除购物车失败-2~~"
        return jsonify(resp)
    return jsonify(resp)
