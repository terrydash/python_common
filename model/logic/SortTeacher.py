from model.base.MongoDBEntity import MongoDBEntity


class SortTeacher(MongoDBEntity):
    actyear = ''
    teachers = list()
    supervison = dict()
    sortresult = ''
    datetime = ''

    def __init__(self, actyear: str, teachers: list, supervison: dict, sortresult: str, datetime: str):
        self.actyear = actyear
        self.teachers = teachers
        self.supervison = supervison
        self.sortresult = sortresult
        self.datetime = datetime
