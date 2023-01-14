from flask import Blueprint

from db.MongoConn import mongodb

commonbp = Blueprint('common', __name__)


@commonbp.route('/mongo')
def getMongo():
    db = mongodb
    result = []
    if db.my is not None:
        for i in db.my.find():
            result.append(i)
    return str(result)
