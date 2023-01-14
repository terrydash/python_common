from bson.json_util import dumps
from flask import Blueprint, request

from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
from model.common.jsonModel import class2json, response_normal, response_error

mainbp = Blueprint('course_scheme', __name__)


@mainbp.route('/get/<id>', methods=["GET"])
def GetCS(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    cel = CourseEvaluateLogic()
    result, num, msg = cel.get_by_id(id)
    r = response_normal(data=result, count=num, msg=msg)

    return r.to_json()


@mainbp.route('/delete', methods=["POST"])
def DeleteCS():
    requestjson = request.json
    _id = requestjson.get('id')
    if len(_id) == 0 or _id is None:
        return response_error(msg='id不能为空！').to_json()
    cel = CourseEvaluateLogic()
    result, num, msg = cel.delete_by_id(_id)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/getall', methods=["GET"])
def GetAllCSNoPage():
    cel = CourseEvaluateLogic()
    results, num, msg = cel.get_all_no_page()
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/getallandfirstindex', methods=["GET"])
def GetAllCSNoPageAndFirstIndex():
    cel = CourseEvaluateLogic()
    results, num, msg = cel.get_all_and_firstindex()
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/get', methods=["GET"])
def GetAllCS():
    page = 1
    pagesize = 10
    name = ''
    sort = '+id'
    if 'page' in request.values:
        page = int(request.values.get('page'))
    if 'name' in request.values:
        name = request.values.get('name')
    if 'pagesize' in request.values:
        pagesize = int(request.values.get('pagesize'))
    if 'sort' in request.values:
        sort = request.values.get('sort')
    cel = CourseEvaluateLogic()
    if name is not None and len(name) > 0:
        results, num, msg = cel.search_page(page, pagesize, name, sort)
    else:
        results, num, msg = cel.get_all_page(page, pagesize, sort)
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/insert', methods=["POST"])
def InsertCS():
    requestjson = request.json
    name = requestjson.get('name')
    if len(name) == 0:
        return dumps(class2json(response_error(data=None, count=0, msg='课程评价方案的名字不能为空！')))
    description = requestjson.get('description')
    remarks = requestjson.get('remarks')
    cel = CourseEvaluateLogic()
    results, num, msg = cel.insert(name, remarks, description)
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/update', methods=["POST"])
def UpdateCS():
    requestjson = request.json
    name = requestjson.get('name')
    if len(name) == 0 or name is None:
        return response_error(data=None, count=0, msg='课程评价方案的名字不能为空！').to_json()
    _id = requestjson.get('_id')
    if len(_id) == 0 or _id is None:
        return response_error(data=None, count=0, msg='要修改的课程评价方案的id不能为空！').to_json()
    description = requestjson.get('description')
    remarks = requestjson.get('remarks')
    cel = CourseEvaluateLogic()
    results, num, msg = cel.update(_id, name, remarks, description)
    return response_normal(data=results, count=num, msg=msg).to_json()
