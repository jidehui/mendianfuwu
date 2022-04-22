# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, Text
from sqlalchemy.schema import FetchedValue
from application import db


class PayOrderItem(db.Model):
    __tablename__ = 'pay_order_item'

    id = db.Column(db.Integer, primary_key=True)
    pay_order_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='订单id')
    member_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='会员id')
    quantity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='购买数量 默认1份')
    price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='商品总价格，售价 * 数量')
    shop_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='美食表id')
    note = db.Column(db.Text, nullable=False, info='备注信息')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态：1：成功 0 失败')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最近一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
