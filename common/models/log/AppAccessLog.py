# coding: utf-8
from application import db


class AppAccessLog(db.Model):
    __tablename__ = 'app_access_log'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='uid')
    referer_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='当前访问的refer')
    target_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='访问的url')
    query_params = db.Column(db.Text, nullable=False, info='get和post参数')
    ua = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='访问ua')
    ip = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='访问ip')
    note = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='json格式备注字段')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
