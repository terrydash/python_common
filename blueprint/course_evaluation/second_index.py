from flask import Blueprint, request

from logic.course_evaluate.SecondIndex import SecondIndexLogic
from model.common.jsonModel import response_normal, response_error

mainbp = Blueprint('second_index', __name__)


@mainbp.route('/get/<id>', methods=["GET"])
def GetCS(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    sil = SecondIndexLogic()
    result, num, msg = sil.get_by_id(id)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/delete', methods=["POST"])
def DeleteCS():
    requestjson = request.json
    _id = requestjson.get('id')
    if len(_id) == 0 or _id is None:
        return response_error(msg='id不能为空！').to_json()
    si = SecondIndexLogic()
    result, num, msg = si.delete_by_id(_id)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/get', methods=["GET"])
def GetAllCS():
    page = 1
    pagesize = 10
    name = ''
    sort = '+id'
    firstindexid = ''
    if 'page' in request.values:
        page = int(request.values.get('page'))
    if 'name' in request.values:
        name = request.values.get('name')
    if 'pagesize' in request.values:
        pagesize = int(request.values.get('pagesize'))
    if 'sort' in request.values:
        sort = request.values.get('sort')
    if 'firstindexid' in request.values:
        firstindexid = request.values.get('firstindexid')
    sil = SecondIndexLogic()
    if (name is not None and len(name) > 0) or (firstindexid is not None and len(firstindexid) > 0):
        results, num, msg = sil.search_page(page, pagesize, name, firstindexid, sort, )
    else:
        results, num, msg = sil.get_all_page(page, pagesize, sort)
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/insert', methods=["POST"])
def InsertCS():
    requestjson = request.json

    if 'model' in requestjson:
        model = dict(requestjson.get('model'))
        sil = SecondIndexLogic()
        result, si, msg = sil.check_model(model)
        if result:
            result, num, msg = sil.insert(si)
            return response_normal(count=num, msg=msg).to_json()
        else:
            response_error(msg=msg).to_json()
    else:
        return response_error(msg='参数不正确!').to_json()
    return response_error(data=requestjson).to_json()


@mainbp.route('/update', methods=["POST"])
def UpdateCS():
    requestjson = request.json
    if 'model' in requestjson:
        model = dict(requestjson.get('model'))
        id = model.get('_id')
        if id is None or len(id) == 0:
            return response_error(msg='参数不正确!').to_json()
        sil = SecondIndexLogic()
        result, si, msg = sil.check_model(model)
        # print(si)
        if result:
            result, num, msg = sil.update(id, si)
            return response_normal(count=num, msg=msg).to_json()
        else:
            response_error(msg=msg).to_json()
    else:
        return response_error(msg='参数不正确!').to_json()
    return response_error(data=requestjson).to_json()
