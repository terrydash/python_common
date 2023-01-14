from flask import Blueprint, request

from common.decorator import need_power
from logic.course_evaluate.FirstIndex import FirstIndexLogic
from model.common.Common import RoleType
from model.common.jsonModel import response_normal, response_error

mainbp = Blueprint('first_index', __name__)


@mainbp.route('/get/<id>', methods=["GET"])
def GetCS(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    fi = FirstIndexLogic()
    result, num, msg = fi.get_by_id(id)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@need_power(roles=[RoleType.Admin.value])
@mainbp.route('/delete', methods=["POST"])
def DeleteCS():
    requestjson = request.json
    _id = requestjson.get('id')
    if len(_id) == 0 or _id is None:
        return response_error(msg='id不能为空！').to_json()
    fi = FirstIndexLogic()
    result, num, msg = fi.delete_by_id(_id)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/getnopage', methods=["GET"])
def GetAllCSPage():
    name = ''
    sort = '+id'
    schemeid = ''
    if 'pagesize' in request.values:
        pagesize = int(request.values.get('pagesize'))
    if 'sort' in request.values:
        sort = request.values.get('sort')
    if 'schemeid' in request.values:
        schemeid = request.values.get('schemeid')
    fi = FirstIndexLogic()
    results, num, msg = fi.search_no_page(name, schemeid, sort, )

    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/get', methods=["GET"])
def GetAllCS():
    page = 1
    pagesize = 10
    name = ''
    sort = '+id'
    schemeid = ''
    if 'page' in request.values:
        page = int(request.values.get('page'))
    if 'name' in request.values:
        name = request.values.get('name')
    if 'pagesize' in request.values:
        pagesize = int(request.values.get('pagesize'))
    if 'sort' in request.values:
        sort = request.values.get('sort')
    if 'schemeid' in request.values:
        schemeid = request.values.get('schemeid')
    fi = FirstIndexLogic()
    if (name is not None and len(name) > 0) or (schemeid is not None and len(schemeid) > 0):
        results, num, msg = fi.search_page(page, pagesize, name, schemeid, sort, )
    else:
        results, num, msg = fi.get_all_page(page, pagesize, sort)
    return response_normal(data=results, count=num, msg=msg).to_json()

@need_power(roles=[RoleType.Admin.value])
@mainbp.route('/insert', methods=["POST"])
def InsertCS():
    requestjson = request.json
    name = requestjson.get('name')
    if len(name) == 0:
        return response_error(data=None, count=0, msg='课程评价方案的名字不能为空！').to_json()
    schemeid = requestjson.get('schemeid')
    if len(schemeid) == 0:
        return response_error(data=None, count=0, msg='必须选择所属方案').to_json()
    issingle = request.json.get('issingle')
    description = requestjson.get('description')
    remarks = requestjson.get('remarks')
    proportion = requestjson.get('proportion')
    secondtypoe = str(requestjson.get('secondIndexType'))
    fi = FirstIndexLogic()
    results, num, msg = fi.insert(name, remarks, description, schemeid, issingle, proportion, secondtypoe)
    return response_normal(data=results, count=num, msg=msg).to_json()

@need_power(roles=[RoleType.Admin.value])
@mainbp.route('/update', methods=["POST"])
def UpdateCS():
    requestjson = request.json
    name = requestjson.get('name')
    if len(name) == 0 or name is None:
        return response_error(data=None, count=0, msg='课程评价方案的名字不能为空！').to_json()
    _id = requestjson.get('_id')
    if len(_id) == 0 or _id is None:
        return response_error(data=None, count=0, msg='要修改的课程评价方案的id不能为空！').to_json()
    schemeid = requestjson.get('schemeid')
    if len(schemeid) == 0:
        return response_error(data=None, count=0, msg='必须选择所属方案').to_json()
    issingle = request.json.get('issingle')
    description = requestjson.get('description')
    remarks = str(requestjson.get('remarks'))
    proportion = str(requestjson.get('proportion'))
    secondtypoe = str(requestjson.get('secondIndexType'))
    fi = FirstIndexLogic()
    results, num, msg = fi.update(_id, name, remarks, description, schemeid, issingle, proportion, secondtypoe)
    return response_normal(data=results, count=num, msg=msg).to_json()
