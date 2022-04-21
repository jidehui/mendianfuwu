# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer
from sqlalchemy.schema import FetchedValue
from application import db


class MemberComments(db.Model):
    __tablename__ = 'member_comments'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='会员id')
    shop_ids = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='商品ids')
    pay_order_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='订单id')
    score = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='评分')
    content = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='评论内容')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
