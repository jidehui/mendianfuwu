# -*- coding: utf-8 -*-
"""
封装 flask 的全局变量 包括 app 数据库等
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from common.libs.UrlManager import UrlManager


# Application类让它继承Flask
class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        # 调用父类
        super(Application, self).__init__(import_name, template_folder=template_folder,
                                          root_path=root_path, static_folder=None)
        # 加载配置文件
        self.config.from_pyfile('config/base_setting.py')
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])

        self.config.from_pyfile('config/local_setting.py')
        self.config.from_pyfile('config/production_setting.py')

        # 重新初始化变量
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + "/web/templates", root_path=os.getcwd())
manager = Manager(app)

"""
此为函数模板设置,将buildStaticUrl、buildUrl注入到模板中去
"""
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
