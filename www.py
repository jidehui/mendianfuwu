# -*- coding: utf-8 -*-
# 加载蓝图 blueprint

from application import app

'''
 统一拦截器
'''
from web.interceptors.Authlnterceptor import *
from web.interceptors.ErrorInterceptor import *

'''
 蓝图功能，对所有的url进行蓝图功能配置
'''
from web.controllers.index import route_index
from web.controllers.user.User import route_user
from web.controllers.static import route_static
from web.controllers.account.Account import route_account
from web.controllers.member.Member import route_member
from web.controllers.shop.Shop import route_shop
from web.controllers.finance.Finance import route_finance
from web.controllers.stat.Stat import route_stat

'''
 引入小程序api
'''
from web.controllers.api import route_api

# url_prefix 链接前缀为/xx
app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_user, url_prefix="/user")
app.register_blueprint(route_static, url_prefix="/static")
app.register_blueprint(route_account, url_prefix="/account")
app.register_blueprint(route_member, url_prefix="/member")
app.register_blueprint(route_shop, url_prefix="/shop")
app.register_blueprint(route_finance, url_prefix="/finance")
app.register_blueprint(route_stat, url_prefix="/stat")

app.register_blueprint(route_api, url_prefix="/api")
