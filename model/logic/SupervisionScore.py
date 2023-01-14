from model.base.MongoDBEntity import MongoDBEntity


class SupervisionScore(MongoDBEntity):
    teacher = object()
    supervision = object()
    scoreinfo=object()
    actyear =''  # 部门
    mm = ''  # 密码

    def __init__(self, zgh, name, xb, bm, mm):
        self._COLLECTION_NAME = self.__class__.__name__.lower()






