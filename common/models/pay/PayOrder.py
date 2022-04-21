# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Index, Integer, Numeric, String, Text
from sqlalchemy.schema import FetchedValue
from application import db, app


class PayOrder(db.Model):
    __tablename__ = 'pay_order'
    __table_args__ = (
        db.Index('idx_member_id_status', 'member_id', 'status'),
    )

    id = db.Column(db.Integer, primary_key=True)
    order_sn = db.Column(db.String(40), nullable=False, unique=True, server_default=db.FetchedValue(), info='随机订单号')
    member_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='会员id')
    total_price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='订单应付金额')
    yun_price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='运费金额')
    pay_price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='订单实付金额')
    pay_sn = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='第三方流水号')
    prepay_id = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='第三方预付id')
    note = db.Column(db.Text, nullable=False, info='备注信息')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
                       info='1：支付完成 0 无效 -1 申请退款 -2 退款中 -9 退款成功  -8 待支付  -7 完成支付待确认')
    express_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
                               info='快递状态，-8 待支付 -7 已付款待发货 1：确认收货 0：失败')
    express_address_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='快递地址id')
    express_info = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='快递信息')
    comment_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='评论状态')
    pay_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='付款到账时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最近一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')

    @property
    def pay_status(self):
        tmp_status = self.status
        if self.status == 1:
            tmp_status = self.express_status
            if self.express_status == 1 and self.comment_status == 0:
                tmp_status = -5
            if self.express_status == 1 and self.comment_status == 1:
                tmp_status = 1
        return tmp_status

    @property
    def status_desc(self):
        return app.config['PAY_STATUS_DISPLAY_MAPPING'][str(self.pay_status)]

    @property
    def order_number(self):
        order_number = self.created_time.strftime("%Y%m%d%H%M%S")
        order_number = order_number + str(self.id).zfill(5)
        return order_number
