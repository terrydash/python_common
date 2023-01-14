# coding:utf-8
import random
import sys
import threading
import datetime
import time
print("start1")
from flask import Flask, request

from config.startupconfig import init_config
from config.systemconfig import get_config
print("start2")
from init import init_schedule
from init.init_flask import init_flask
print("start3")
from init.init_logging import init_log, get_logger
print("start4")
from logic.common.Login import GetUserInfoFromToken
from model.common.jsonModel import response_normal, response_error

init_log()
sys.setrecursionlimit(10000)
config = init_config
app = Flask(__name__)
init_flask(app)
logger = get_logger(__name__)


@app.after_request
def after_request1(response):
    # response.headers['Access-Control-Allow-Origin'] = "*"
    # response.headers['Access-Control-Allow-Headers']="X-Requested-With,Content-Type,Auth"
    # response.headers['Access-Control-Allow-Methods']="PUT,POST,GET,DELETE,OPTIONS"
    response.headers['Access-Control-Allow-Methods'] = "PUT,POST,GET,DELETE,OPTIONS"
    # app.logger.info('cqrs')
    # print(request.method)
    if (str(request.method).upper() == "OPTIONS"):
        return response
    url = request.full_path
    tokenresult, userinfo = GetUserInfoFromToken()

    requestjson = ""
    if request.json is not None:
        requestjson = str(request.json)
    requestvalue = str(request.values.to_dict())
    requestform = str(request.form.to_dict())
    msg = 'userinfo:' + str(userinfo) + ' method:' + request.method + ' url:' + url + ' requestjson:' + str(
        requestjson) + ' requestvalue:' + requestvalue + ' requestform:' + str(requestform)
    # logger.debug(msg)

    return response


msg = '试用期限已过，请购买激活码！'


# @app.before_request
# def before_request():
#     ip = request.remote_addr
#     url = request.url
#     print(ip)
#     print(url)
#     from init.init_logging import get_logger
#
#     logger.debug('ip:' + ip + ' ' + 'path:' + str(request.path) + ' params:' + str(request.json) + ' ' +
#                  str(request.form) + ' ' + str(request.data))
#     rnd = random.randint(1, 10)
#     if rnd >= 7:
#         time.sleep(rnd / 2)
#         return response_error(msg="网络错误").to_json()
#     if (str(request.path).rstrip(r"/").lower() == r"/config/activatecode"):
#         pass
#     else:
#         from logic.common.Config import ConfigLogic
#         cl = ConfigLogic()
#         activatecode = get_config("activecode")
#         print("ac:" + activatecode)
#         result, message = cl.checkActivateCode(activatecode)
#         if not result:
#             return response_error(msg=message).to_json()


@app.route("/error")
def geterror():
    raise Exception('自定义的错误')


@app.route("/")
def test():
    return str('hello-world')


@app.route("/jsxxb")
def testjsxxb():
    from logic.jwxt.Department import DepartmentLogic
    res = DepartmentLogic().oracle2mongo()
    return response_normal(data=res).to_json()


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    # t = threading.Thread(target=init_schedule.start, daemon=True)
    # t.start()

    app.run(port=config.port, host=config.ip, debug=config.debug)
