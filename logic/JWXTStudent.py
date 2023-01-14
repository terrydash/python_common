from db.OracleConn import DBSession
from model.oracle.xsjbxxb import Xsjbxxb


def getXsjbxx(xh):
    if isinstance(xh, str):
        session=DBSession()
        stu = session.query(Xsjbxxb.xh,Xsjbxxb.xm).filter(Xsjbxxb.xh.like(xh)).one()
        if stu is not None:
            return stu
        else:
            return None
    else:
        raise Exception('学生学号应该为字符串格式')



