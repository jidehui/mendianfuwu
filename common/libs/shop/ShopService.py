# -*- coding: utf-8 -*-
from application import app, db
from common.models.shop.ShopStockChangeLog import ShopStockChangeLog
from common.models.shop.Shop import Shop
from common.libs.Helper import getCurrentDate


class ShopService():

    @staticmethod
    def setStockChangeLog(shop_id=0, quantity=0, note=''):

        if shop_id < 1:
            return False

        shop_info = Shop.query.filter_by(id=shop_id).first()
        if not shop_info:
            return False

        model_stock_change = ShopStockChangeLog()
        model_stock_change.shop_id = shop_id
        model_stock_change.unit = quantity
        model_stock_change.total_stock = shop_info.stock
        model_stock_change.note = note
        model_stock_change.created_time = getCurrentDate()
        db.session.add(model_stock_change)
        db.session.commit()
        return True
