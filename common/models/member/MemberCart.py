# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer
from sqlalchemy.schema import FetchedValue
from application import db


class MemberCart(db.Model):
    __tablename__ = 'member_cart'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='会员id')
    shop_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='商品id')
    quantity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数量')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
