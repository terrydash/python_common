from flask import jsonify, Blueprint

from common.convert import class2json
from model.common.jsonModel import response_error

mainbp = Blueprint('customerror', __name__)


@mainbp.app_errorhandler(500)
def handlererror(e):
    r = response_error(data=str(e))
    return jsonify(class2json(r))


@mainbp.app_errorhandler(404)
def handlernotfounderror(e):
    r = response_error(data=None, msg='请求地址不正确！')
    return jsonify(class2json(r))


@mainbp.route('/error')
def geterr():
    raise Exception('产生自定义错误！')
    r = response_error()
    return jsonify(class2json(r))
