from flask import request

from blueprint import *
from blueprint.course_evaluation import *
from blueprint.jwxt import *
from blueprint.score import score
from blueprint.sortteacher import sortteacher
from blueprint.system import *
from blueprint.data import export
from config.systemconfig import init as sys_config_init
from init.init_logging import get_logger
from logic.common.Login import GetUserInfoFromToken

logger = get_logger(__name__)


def init_flask(app):
    from flask_cors import CORS
    from flask import jsonify
    from model.common.jsonModel import response_error
    from common.convert import class2json
    from logic.common.Cache import CacheLogic
    CacheLogic().init()
    sys_config_init()

    @app.errorhandler(500)
    def handle_invalid_usage(e):
        url = request.full_path
        tokenresult, userinfo = GetUserInfoFromToken()
        requestjson = request.json
        requestvalue = request.values.to_dict()
        requestform = request.form.to_dict()
        msg = 'userinfo:' + str(userinfo) + ' method:' + request.method + ' url:' + url + ' requestjson:' + str(
            requestjson) + ' requestvalue:' + ' requestform:' + str(requestform) + ' error:' + str(e)
        logger.error(msg)
        r = response_error(data=str(e))
        return jsonify(class2json(r))

    @app.errorhandler(404)
    def error(e):
        url = request.full_path
        tokenresult, userinfo = GetUserInfoFromToken()
        requestjson = request.json
        requestvalue = request.values.to_dict()
        requestform = request.form.to_dict()
        msg = 'userinfo:' + str(userinfo) + ' method:' + request.method + ' url:' + url + ' requestjson:' + str(
            requestjson) + ' requestvalue:' + ' requestform:' + str(requestform) + ' error:' + str(e)
        logger.error(msg)
        r = response_error(data=str(e))
        return jsonify(class2json(r))

    CORS(app, supports_credentials=True)
    '''
    import rsa
    (pubkey, privkey) = rsa.newkeys(1024)
    with open('public.pem','w+') as f:
        f.write(pubkey.save_pkcs1().decode())

    with open('private.pem','w+') as f:
        f.write(privkey.save_pkcs1().decode())
    '''
    # app.register_blueprint(errorbp)
    app.register_blueprint(common.commonbp)
    app.register_blueprint(login.loginbp, url_prefix='/login')
    app.register_blueprint(admin.adminbp, url_prefix='/admin')
    app.register_blueprint(test.mainbp, url_prefix='/test')
    app.register_blueprint(first_index.mainbp, url_prefix='/firstindex')
    app.register_blueprint(course_scheme.mainbp, url_prefix='/coursescheme')
    app.register_blueprint(second_index.mainbp, url_prefix='/secondindex')
    app.register_blueprint(config.mainbp, url_prefix='/config')
    app.register_blueprint(department.mainbp, url_prefix='/dept')
    app.register_blueprint(teacher.mainbp, url_prefix='/teacher')
    app.register_blueprint(teachtask.mainbp, url_prefix='/teachtask')
    app.register_blueprint(schedule.mainbp, url_prefix='/schedule')
    app.register_blueprint(supervision.mainbp, url_prefix='/supervision')
    app.register_blueprint(deptmanager.mainbp, url_prefix='/deptmanager')
    app.register_blueprint(score.mainbp, url_prefix='/score')
    app.register_blueprint(sortteacher.mainbp, url_prefix='/sortteacher')
    app.register_blueprint(manager.mainbp, url_prefix='/manager')
    app.register_blueprint(export.exportbp, url_prefix='/data')
