from flask import Blueprint, request

from logic.jwxt.TeachTask import TeachTaskLogic
from logic.jwxt.Teacher import TeacherLogic
from model.common.jsonModel import response_normal, response_error

ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])
mainbp = Blueprint('teachtask', __name__)


def allowed_file(filename):
    find = False;
    extname = filename.rsplit('.', 1)[1]
    for x in ALLOWED_EXTENSIONS:
        if str(extname).upper() == str(x).upper():
            find = True
    return find


@mainbp.route('/get/<id>', methods=["GET"])
def GetDepartment(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    tl = TeachTaskLogic()
    result, num, msg = tl.get_by_id(id)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/upload', methods=["POST"])
def uploadfile():
    f = request.files['file']
    if not allowed_file(f.filename):
        return response_error(msg="文件类型不允许，只允许xls或者xlsx").to_json()
    from logic.jwxt.TeachTask import TeachTaskLogic
    ttl = TeachTaskLogic()
    result, msg = ttl.loadxlsx(f.stream.read())
    if result:
        return response_normal(data=f.filename).to_json()
    else:
        return response_error(msg=msg).to_json()


@mainbp.route('/gettemplate', methods=["GET", "POST"])
def downloadfile():
    from enviroment import project_dir
    import os
    fullfilename = project_dir + os.sep + "template" + os.sep + "teachtask_template.xlsx"
    print(fullfilename)
    filename = "教学任务模板"
    if not os.path.exists(fullfilename):
        return response_error("模板文件不存在").to_json()
    from flask import send_file, make_response
    response = make_response(send_file(fullfilename))
    return response


@mainbp.route('/sync', methods=["GET"])
def GetOracle2Mongo():
    ttl = TeachTaskLogic()
    try:
        ttl.oracle2mongo()
        ttl.xxkjxrw_oracle2mongo()
    except Exception as e:
        return response_error(data=False, count=0, msg=str(e))

    return response_normal(data=True, count=0, msg='正常').to_json()


@mainbp.route('/get', methods=["GET"])
def GetAllTeachTask():
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
    ttl = TeachTaskLogic()
    # print(name, dept, sort,page,pagesize)
    if (name is not None and len(name) > 0) or (dept is not None and len(dept) > 0):
        results, num, msg = ttl.search_page(page=page, pagesize=pagesize, query={'name': name, 'dept': dept}, sort=sort)
    else:
        results, num, msg = ttl.get_all_page(page, pagesize, sort)
    # 去掉密码
    for x in results:
        if 'mm' in x:
            x.pop('mm')
    return response_normal(data=results, count=num, msg=msg).to_json()
