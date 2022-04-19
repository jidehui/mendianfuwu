# -*- coding: utf-8 -*-
# 本地开发调试需要，云服务器不需要，不然加载不到资源文件夹如显示不到图片

from flask import Blueprint, send_from_directory
from application import app

# 定义一个蓝图 实例变量 route_static，然后传进去一个__name__作为内置对应程序名称
route_static = Blueprint('static', __name__)


# 注册路由 通过/ 访问我们的路由 资源
@route_static.route("/<path:filename>")
def index(filename):
    # app.logger.info(filename)
    return send_from_directory(app.root_path + "/web/static", filename)
