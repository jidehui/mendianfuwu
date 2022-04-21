# -*- coding: utf-8 -*-
from web.controllers.api import route_api
from flask import request, jsonify, g
from common.models.shop.ShopCat import ShopCat
from common.models.shop.Shop import Shop
from common.models.member.MemberCart import MemberCart
from common.models.member.MemberComments import MemberComments
from common.models.member.Member import Member
from common.libs.UrlManager import UrlManager
from common.libs.Helper import getCurrentDate, getDictFilterField, selectFilterObj
from application import app, db
from sqlalchemy import or_


@route_api.route("/shop/index")
def shopIndex():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    cat_list = ShopCat.query.filter_by(status=1).order_by(ShopCat.weight.desc()).all()
    data_cat_list = []
    data_cat_list.append({
        'id': 0,
        'name': "全部"
    })
    if cat_list:
        for item in cat_list:
            tmp_data = {
                'id': item.id,
                'name': item.name
            }
            data_cat_list.append(tmp_data)
    resp['data']['cat_list'] = data_cat_list

    shop_list = Shop.query.filter_by(status=1) \
        .order_by(Shop.total_count.desc(), Shop.id.desc()).limit(3).all()

    data_shop_list = []
    if shop_list:
        for item in shop_list:
            tmp_data = {
                'id': item.id,
                'pic_url': UrlManager.buildImageUrl(item.main_image)
            }
            data_shop_list.append(tmp_data)

    resp['data']['banner_list'] = data_shop_list
    return jsonify(resp)


@route_api.route("/shop/search")
def shopSearch():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    cat_id = int(req['cat_id']) if 'cat_id' in req else 0
    mix_kw = str(req['mix_kw']) if 'mix_kw' in req else ''
    p = int(req['p']) if 'p' in req else 1

    if p < 1:
        p = 1

    page_size = 10
    offset = (p - 1) * page_size
    query = Shop.query.filter_by(status=1)
    if cat_id > 0:
        query = query.filter_by(cat_id=cat_id)

    if mix_kw:
        rule = or_(Shop.name.ilike("%{0}%".format(mix_kw)), Shop.tags.ilike("%{0}%".format(mix_kw)))
        query = query.filter(rule)

    shop_list = query.order_by(Shop.total_count.desc(), Shop.id.desc()) \
        .offset(offset).limit(page_size).all()

    data_shop_list = []
    if shop_list:
        for item in shop_list:
            tmp_data = {
                'id': item.id,
                'name': "%s" % (item.name),
                'price': str(item.price),
                'min_price': str(item.price),
                'pic_url': UrlManager.buildImageUrl(item.main_image)
            }
            data_shop_list.append(tmp_data)
    resp['data']['list'] = data_shop_list
    resp['data']['has_more'] = 0 if len(data_shop_list) < page_size else 1
    return jsonify(resp)


@route_api.route("/shop/info")
def shopInfo():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req else 0
    shop_info = Shop.query.filter_by(id=id).first()
    if not shop_info or not shop_info.status:
        resp['code'] = -1
        resp['msg'] = "美食已下架"
        return jsonify(resp)

    member_info = g.member_info
    cart_number = 0
    if member_info:
        cart_number = MemberCart.query.filter_by(member_id=member_info.id).count()
    resp['data']['info'] = {
        "id": shop_info.id,
        "name": shop_info.name,
        "summary": shop_info.summary,
        "total_count": shop_info.total_count,
        "comment_count": shop_info.comment_count,
        'main_image': UrlManager.buildImageUrl(shop_info.main_image),
        "price": str(shop_info.price),
        "stock": shop_info.stock,
        "pics": [UrlManager.buildImageUrl(shop_info.main_image)]
    }
    resp['data']['cart_number'] = cart_number
    return jsonify(resp)


@route_api.route("/shop/comments")
def shopComments():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req else 0
    query = MemberComments.query.filter(MemberComments.shop_ids.ilike("%_{0}_%".format(id)))
    list = query.order_by(MemberComments.id.desc()).limit(5).all()
    data_list = []
    if list:
        member_map = getDictFilterField(Member, Member.id, "id", selectFilterObj(list, "member_id"))
        for item in list:
            if item.member_id not in member_map:
                continue
            tmp_member_info = member_map[item.member_id]
            tmp_data = {
                'score': item.score_desc,
                'date': item.created_time.strftime("%Y-%m-%d %H:%M:%S"),
                "content": item.content,
                "user": {
                    'nickname': tmp_member_info.nickname,
                    'avatar_url': tmp_member_info.avatar,
                }
            }
            data_list.append(tmp_data)
    resp['data']['list'] = data_list
    resp['data']['count'] = query.count()
    return jsonify(resp)
