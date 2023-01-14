from flask import Blueprint, request

from logic.jwxt.Department import DepartmentLogic
from logic.jwxt.Teacher import TeacherLogic
from model.common.jsonModel import response_normal, response_error

mainbp = Blueprint('teacher', __name__)


@mainbp.route('/get/<id>', methods=["GET"])
def GetDepartment(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    tl = TeacherLogic()
    # result, num, msg = tl.get_by_id(id)
    result, num, msg = tl.get_pass_by_id(id)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/oracle2mongo', methods=["GET"])
def GetOracle2Mongo():
    tl = TeacherLogic()
    results = tl.oracle2mongo()
    return response_normal(data=None, count=len(results), msg='正常').to_json()


@mainbp.route('/get', methods=["GET"])
def GetAllDepartment():
    page = 1
    pagesize = 10
    name = ''
    sort = '+id'
    dept = ''
    if 'page' in request.values:
        page = int(request.values.get('page'))
    if 'name' in request.values:
        name = request.values.get('name')
    if 'pagesize' in request.values:
        pagesize = int(request.values.get('pagesize'))
    if 'sort' in request.values:
        sort = request.values.get('sort')
    if 'dept' in request.values:
        dept = request.values.get('dept')
    tl = TeacherLogic()
    # print(name, dept)
    if (name is not None and len(name) > 0) or (dept is not None and len(dept) > 0):
        results, num, msg = tl.search_page(page=page, pagesize=pagesize, query={'name': name, 'dept': dept}, sort=sort)
    else:
        results, num, msg = tl.get_all_page(page, pagesize, sort)
    # 去掉密码
    for x in results:
        if 'mm' in x:
            x.pop('mm')
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
