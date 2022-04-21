# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, redirect
from common.libs.Helper import ops_render, getCurrentDate, iPagination, getDictFilterField
from application import app, db
from common.models.shop.Shop import Shop
from common.models.shop.ShopCat import ShopCat
from common.models.shop.ShopStockChangeLog import ShopStockChangeLog
from common.libs.UrlManager import UrlManager
from common.libs.shop.ShopService import ShopService
from decimal import Decimal
from sqlalchemy import or_

route_shop = Blueprint('shop_page', __name__)


@route_shop.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    query = Shop.query
    if 'mix_kw' in req:
        rule = or_(Shop.name.ilike("%{0}%".format(req['mix_kw'])), Shop.tags.ilike("%{0}%".format(req['mix_kw'])))
        query = query.filter(rule)

    if 'status' in req and int(req['status']) > -1:
        query = query.filter(Shop.status == int(req['status']))

    if 'cat_id' in req and int(req['cat_id']) > 0:
        query = query.filter(Shop.cat_id == int(req['cat_id']))

    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace("&p={}".format(page), "")
    }

    pages = iPagination(page_params)
    offset = (page - 1) * app.config['PAGE_SIZE']
    list = query.order_by(Shop.id.desc()).offset(offset).limit(app.config['PAGE_SIZE']).all()

    cat_mapping = getDictFilterField(ShopCat, ShopCat.id, "id", [])
    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['search_con'] = req
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    resp_data['cat_mapping'] = cat_mapping
    resp_data['current'] = 'index'
    return ops_render("shop/index.html", resp_data)


@route_shop.route("/info")
def info():
    resp_data = {}
    req = request.args
    id = int(req.get("id", 0))
    reback_url = UrlManager.buildUrl("/shop/index")

    if id < 1:
        return redirect(reback_url)

    info = Shop.query.filter_by(id=id).first()
    if not info:
        return redirect(reback_url)

    stock_change_list = ShopStockChangeLog.query.filter(ShopStockChangeLog.shop_id == id) \
        .order_by(ShopStockChangeLog.id.desc()).all()

    resp_data['info'] = info
    resp_data['stock_change_list'] = stock_change_list
    resp_data['current'] = 'index'
    return ops_render("shop/info.html", resp_data)


@route_shop.route("/set", methods=['GET', 'POST'])
def set():
    if request.method == "GET":
        resp_data = {}
        req = request.args
        id = int(req.get('id', 0))
        info = Shop.query.filter_by(id=id).first()
        if info and info.status != 1:
            return redirect(UrlManager.buildUrl("/shop/index"))

        cat_list = ShopCat.query.all()
        resp_data['info'] = info
        resp_data['cat_list'] = cat_list
        resp_data['current'] = 'index'
        return ops_render("shop/set.html", resp_data)

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req and req['id'] else 0
    cat_id = int(req['cat_id']) if 'cat_id' in req else 0
    name = req['name'] if 'name' in req else ''
    price = req['price'] if 'price' in req else ''
    main_image = req['main_image'] if 'main_image' in req else ''
    summary = req['summary'] if 'summary' in req else ''
    stock = int(req['stock']) if 'stock' in req else ''
    tags = req['tags'] if 'tags' in req else ''

    if cat_id < 1:
        resp['code'] = -1
        resp['msg'] = "请选择分类~~"
        return jsonify(resp)

    if name is None or len(name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的名称~~"
        return jsonify(resp)

    if not price or len(price) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)

    price = Decimal(price).quantize(Decimal('0.00'))
    if price <= 0:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)

    if main_image is None or len(main_image) < 3:
        resp['code'] = -1
        resp['msg'] = "请上传封面图~~"
        return jsonify(resp)

    if summary is None or len(summary) < 3:
        resp['code'] = -1
        resp['msg'] = "请输入图书描述，并不能少于10个字符~~"
        return jsonify(resp)

    if stock < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的库存量~~"
        return jsonify(resp)

    if tags is None or len(tags) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入标签，便于搜索~~"
        return jsonify(resp)

    shop_info = Shop.query.filter_by(id=id).first()
    before_stock = 0
    if shop_info:
        model_shop = shop_info
        before_stock = model_shop.stock
    else:
        model_shop = Shop()
        model_shop.status = 1
        model_shop.created_time = getCurrentDate()

    model_shop.cat_id = cat_id
    model_shop.name = name
    model_shop.price = price
    model_shop.main_image = main_image
    model_shop.summary = summary
    model_shop.stock = stock
    model_shop.tags = tags
    model_shop.updated_time = getCurrentDate()

    db.session.add(model_shop)
    ret = db.session.commit()

    ShopService.setStockChangeLog(model_shop.id, int(stock) - int(before_stock), "后台修改")
    return jsonify(resp)


@route_shop.route("/cat")
def cat():
    resp_data = {}
    req = request.values
    query = ShopCat.query

    if 'status' in req and int(req['status']) > -1:
        query = query.filter(ShopCat.status == int(req['status']))

    list = query.order_by(ShopCat.weight.desc(), ShopCat.id.desc()).all()
    resp_data['list'] = list
    resp_data['search_con'] = req
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    resp_data['current'] = 'cat'
    return ops_render("shop/cat.html", resp_data)


@route_shop.route("/cat-set", methods=["GET", "POST"])
def catSet():
    if request.method == "GET":
        resp_data = {}
        req = request.args
        id = int(req.get("id", 0))
        info = None
        if id:
            info = ShopCat.query.filter_by(id=id).first()
        resp_data['info'] = info
        resp_data['current'] = 'cat'
        return ops_render("shop/cat_set.html", resp_data)

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values

    id = req['id'] if 'id' in req else 0
    name = req['name'] if 'name' in req else ''
    weight = int(req['weight']) if ('weight' in req and int(req['weight']) > 0) else 1

    if name is None or len(name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的分类名称~~"
        return jsonify(resp)

    shop_cat_info = ShopCat.query.filter_by(id=id).first()
    if shop_cat_info:
        model_shop_cat = shop_cat_info
    else:
        model_shop_cat = ShopCat()
        model_shop_cat.created_time = getCurrentDate()
    model_shop_cat.name = name
    model_shop_cat.weight = weight
    model_shop_cat.updated_time = getCurrentDate()
    db.session.add(model_shop_cat)
    db.session.commit()
    return jsonify(resp)


@route_shop.route("/cat-ops", methods=["POST"])
def catOps():
    resp = {'code': 200, 'msg': '操作成功!', 'data': {}}
    req = request.values

    id = req['id'] if 'id' in req else 0
    act = req['act'] if 'act' in req else ''
    if not id:
        resp['code'] = -1
        resp['msg'] = "请选择要操作的账号~~"
        return jsonify(resp)

    if act not in ['remove', 'recover']:
        resp['code'] = -1
        resp['msg'] = "操作有误，请重试~~"
        return jsonify(resp)

    shop_cat_info = ShopCat.query.filter_by(id=id).first()
    if not shop_cat_info:
        resp['code'] = -1
        resp['msg'] = "指定分类不存在~~"
        return jsonify(resp)

    if act == "remove":
        shop_cat_info.status = 0
    elif act == "recover":
        shop_cat_info.status = 1

        shop_cat_info.update_time = getCurrentDate()
    db.session.add(shop_cat_info)
    db.session.commit()
    return jsonify(resp)


@route_shop.route("/ops", methods=["POST"])
def ops():
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values

    id = req['id'] if 'id' in req else 0
    act = req['act'] if 'act' in req else ''

    if not id:
        resp['code'] = -1
        resp['msg'] = "请选择要操作的账号~~"
        return jsonify(resp)

    if act not in ['remove', 'recover']:
        resp['code'] = -1
        resp['msg'] = "操作有误，请重试~~"
        return jsonify(resp)

    shop_info = Shop.query.filter_by(id=id).first()
    if not shop_info:
        resp['code'] = -1
        resp['msg'] = "指定美食不存在~~"
        return jsonify(resp)

    if act == "remove":
        shop_info.status = 0
    elif act == "recover":
        shop_info.status = 1

    shop_info.updated_time = getCurrentDate()
    db.session.add(shop_info)
    db.session.commit()
    return jsonify(resp)
