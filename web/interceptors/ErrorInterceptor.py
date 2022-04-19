# -*- coding: utf-8 -*-
from application import app
from common.libs.Helper import ops_render
from common.libs.LogService import LogService


@app.errorhandler(404)
def error_404(e):
    LogService.addErrorLog(str(e))
    return ops_render('error/error.html', {'status': 404, 'msg_code': '404', 'msg': '很抱歉，这里什么都没有，放过我吧!'})
