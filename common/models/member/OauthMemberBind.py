# coding: utf-8
from application import db


class OauthMemberBind(db.Model):
    __tablename__ = 'oauth_member_bind'
    __table_args__ = (
        db.Index('idx_type_openid', 'type', 'openid'),
    )

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='会员id')
    client_type = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(),
                            info='客户端来源类型。qq,weibo,weixin')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型 type 1:wechat ')
    openid = db.Column(db.String(80), nullable=False, server_default=db.FetchedValue(), info='第三方id')
    unionid = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    extra = db.Column(db.Text, nullable=False, info='额外字段')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
