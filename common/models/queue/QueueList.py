# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class QueueList(db.Model):
    __tablename__ = 'queue_list'

    id = db.Column(db.Integer, primary_key=True)
    queue_name = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='队列名字')
    data = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue(), info='队列数据')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 -1 待处理 1 已处理')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
