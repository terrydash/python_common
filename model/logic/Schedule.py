from model.base.MongoDBEntity import MongoDBEntity


class Schedule(MongoDBEntity):

    def __init__(self):
        self._COLLECTION_NAME = self.__class__.__name__.lower()
        #   self.tjkbdm = ''
        self.xqj = 0
        self.sjdxh = 0
        self.xkkh = ''
        self.qssj = 0
        self.jssj = 0
        self.dsz = ''
        self.kcdm = ''
        self.jsbh = ''
        self.jszgh = ''
        self.zws = 0
        self.sknr = ''
        self.qssjd = 0
        self.qhbz = ''
        self.yxxxk = ''
        self.syycsk = ''
