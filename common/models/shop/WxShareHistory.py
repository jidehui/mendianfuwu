# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class WxShareHistory(db.Model):
    __tablename__ = 'wx_share_history'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='会员id')
    share_url = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='分享的页面url')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
