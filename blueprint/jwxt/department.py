from flask import Blueprint, request

from common.decorator import need_power
from logic.jwxt.Department import DepartmentLogic
from model.common.Common import RoleType
from model.common.jsonModel import response_normal, response_error

mainbp = Blueprint('department', __name__)


@mainbp.route('/get/<id>', methods=["GET"])
def GetDepartment(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    dl = DepartmentLogic()
    result, num, msg = dl.get_by_id(id)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/getteachdept', methods=["GET"])
def GetAllTeachDepartment():
    dl = DepartmentLogic()
    results, num, msg = dl.get_all_teach_dept()
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/get', methods=["GET"])
@need_power(roles=[RoleType.Admin.value])
def GetAllDepartmentPage():
    page = 1
    pagesize = 10
    sort = '+_id'
    if 'page' in request.values:
        page = int(request.values.get('page'))
    if 'pagesize' in request.values:
        pagesize = int(request.values.get('pagesize'))
    if 'sort' in request.values:
        sort = request.values.get('sort')
    dl = DepartmentLogic()
    results, num, msg = dl.get_all_page(page, pagesize, sort)
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/getall', methods=["GET"])
@need_power(roles=[RoleType.Admin.value])
def GetAllDepartments():
    dl = DepartmentLogic()
    results, num, msg = dl.get_all_fromdb()
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/update', methods=["POST"])
def UpdateDepartment():
    requestjson = request.json
    if 'model' in requestjson:
        model = dict(requestjson.get('model'))
        dept = {}
        id = model.get('_id')
        if id is None or len(id) == 0:
            return response_error(msg='参数不正确!').to_json()
        dl = DepartmentLogic()
        if 'othername' in model.keys() and len(model.get('othername')) > 0:
            dept = {'othername': model.get('othername')}
        else:
            return response_error(msg='别名不能为空！').to_json()
        if 'is_teach_dept' in model.keys() and len(str(model.get('is_teach_dept'))) > 0:
            dept['is_teach_dept'] = model.get('is_teach_dept')
        result, num, msg = dl.update(id, dept)
        return response_normal(data=result, count=num, msg=msg).to_json()

    return response_error(msg='参数不正确!').to_json()
