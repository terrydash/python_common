import datetime

from common.convert import class2json
from config.systemconfig import get_config
from logic.Base import BaseLogic
from model.logic.Config import Config
from repository.BaseRepository import BaseRepository


class ConfigLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = str(Config().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def update(self, id, model: dict):
        config, num, msg = self.baseRepository.get_by_id(id)
        if config is None:
            raise Exception("不存在ID的配置项")
        if "value" in config and "value" in model:
            config["value"] = model["value"]
            result, num, msg = self.baseRepository.update_by_id(id, class2json(model))
            return True
        else:
            return False

    def getCurrentXN(self):
        from config.systemconfig import xn
        if len(xn) > 0:
            return xn
        xn = get_config('xn')
        return xn

    def getMAX_A(self):
        from config.const.configConst import SORT_MAX_A
        return get_config(SORT_MAX_A)

    def getSortTeacherIsOpen(self):
        from config.const.configConst import CAN_SORT_TEACHER
        return get_config(CAN_SORT_TEACHER)

    def getCurrentXQ(self):
        from config.systemconfig import xq
        if len(xq) > 0:
            return xq
        xq = get_config('xq')
        return xq

    def getCurrentActYear(self):
        from config.systemconfig import actyear
        if len(actyear) > 0:
            return actyear
        actyear = self.getCurrentXN() + '-' + self.getCurrentXQ()
        return actyear

    def checkActivateCode(self, activatecode: str):
        dec_activatecode = ""
        activatedate = ""
        from logic.common.Password import prpcrypt
        from mainflask import msg
        try:

            dec_activatecode = str(prpcrypt.password_decrypt(activatecode))
            if len(dec_activatecode) == 0:
                return False, msg
            actlist = list(dec_activatecode.split("-"))
            if len(actlist) < 4:
                return False, msg

            ac_year = str(actlist[1])
            ac_month = str(actlist[2])
            ac_day = str(actlist[3])
            activatecodedate = ac_year + '-' + ac_month + '-' + ac_day
            activetime = datetime.datetime.strptime(activatecodedate, "%Y-%m-%d")
            nowtime = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
            leftdays = int((activetime - nowtime).days)
            activatedate = activetime
            print(activetime)
            print(nowtime)
            print(leftdays)
            print(leftdays < 0)
            if leftdays < 0:
                return False, msg
        except Exception as e:
            print(str(e))
            return False, msg + '(激活码不正确:错误信息为' + str(e) + ')'
        return True, str(activatedate)

    def updateActiveCode(self, activatecode: str):
        result, num, msg = self.baseRepository.search_no_page({'name': 'activecode'})
        print(num)
        if result is not None and type(result) is list and len(result) > 0 and len(activatecode) > 0:
            ac_config = result[0]
            print(ac_config)
            ac_config['value'] = activatecode.strip()
            self.baseRepository.update_by_id(str(ac_config['_id']), ac_config)
            from config.systemconfig import init
            init()
