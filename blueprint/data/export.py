import io

from flask import Blueprint, request, make_response, send_file

from common.decorator import need_power
from logic.jwxt.Department import DepartmentLogic
from logic.data.Export import DataExportLogic
from model.common.Common import RoleType
from model.common.jsonModel import response_normal, response_error, response_notlogin

exportbp = Blueprint('export', __name__)


@exportbp.route('/getexport', methods=["POST"])
def getexport():
    teacher_name = ''
    dept = ''
    schemeid = ''
    actyear = ''
    requestjson = request.json
    print(requestjson)
    if requestjson is not None:
        if 'name' in requestjson:
            teacher_name = requestjson.get('name')
        if 'dept' in requestjson:
            dept = requestjson.get('dept')
        if 'actyear' in requestjson:
            actyear = requestjson.get('actyear')
        if 'schemeid' in requestjson:
            schemeid = str(requestjson.get('schemeid'))
    from logic.common.Login import GetUserInfoFromToken
    result, _ = GetUserInfoFromToken()
    if result:
        dl = DataExportLogic()
        wb = dl.export_all_bm_score(teacher_name=teacher_name, dept=dept, actyear=actyear, schemeid=schemeid)
        sio = io.BytesIO()
        wb.save(sio)
        sio.seek(0)
        return send_file(sio, mimetype='application/vnd.ms-excel')
    return response_notlogin().to_json()
