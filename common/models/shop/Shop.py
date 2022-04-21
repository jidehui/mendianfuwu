# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue
from application import db


class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分类id')
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='书籍名称')
    price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='售卖金额')
    main_image = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='主图')
    summary = db.Column(db.String(10000), nullable=False, server_default=db.FetchedValue(), info='描述')
    stock = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='库存量')
    tags = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='tag关键字，以","连接')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 1：有效 0：无效')
    month_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='月销售数量')
    total_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='总销售量')
    view_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='总浏览次数')
    comment_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='总评论量')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后插入时间')
