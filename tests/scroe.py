import unittest

import re
from config.startupconfig import init_config


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        self.config = init_config

    # 销毁
    def tearDown(self):
        pass

    def test_get_course_info_and_scheme(self):
        from logic.score.Score import ScoreLogic
        sl = ScoreLogic()
        result = sl.get_course_info_and_scheme(xkkh='(2018-2019-1)-0030308051-070149-1',
                                               schemeid='5b7482e9d72e2316cc2bf3c2')
        # print(dumps(class2json(result)))

    def test_clear_images(self):
        from logic.score.Score import ScoreLogic
        from model.logic.Score import Score
        from common.convert import class2json
        sl = ScoreLogic()
        from repository.BaseRepository import BaseRepository
        self.collectionName = str(Score().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)
        result, num, msg = self.baseRepository.get_all_no_page()
        for x in result:
            x = dict(x)
            haserr = False
            zz = r"<img[^>]*>"
            pattern1 = re.compile(zz)
            if len(str(x["content"])) > 5000:
                x["content"] = re.sub(zz, "", str(x["content"]))
                haserr = True
            if len(str(x["comment"])) > 5000:
                x["comment"] = re.sub(zz, "", str(x["comment"]))
                haserr = True
            if haserr:
                id = str(x["_id"])
                print(id)
                self.baseRepository.update_by_id(_id=id, entity=x)

    def test_replace_JSZGH_length_more_than_six(self):
        from logic.score.Score import ScoreLogic
        from model.logic.Score import Score

        sl = ScoreLogic()
        from repository.BaseRepository import BaseRepository
        self.collectionName = str(Score().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)
        result, num, msg = self.baseRepository.get_all_no_page()
        for x in result:
            x = dict(x)
            jszgh = x.get('jszgh')
            if len(str(jszgh)) > 6:
                id = str(x.get("_id"))
                x['jszgh'] = str(jszgh)[0:6]
                self.baseRepository.update_by_id(id, x)
                print(x)

        print(num)
        print(msg)

    def test_replace_JSZGH_length_more_than_six2(self):
        from logic.jwxt.TeachTask import TeachTaskLogic
        from model.logic.TeachTask import TeachTask

        sl = TeachTaskLogic()
        from repository.BaseRepository import BaseRepository
        self.collectionName = str(TeachTask().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)
        result, num, msg = self.baseRepository.get_all_no_page()
        for x in result:
            x = dict(x)
            jszgh = x.get('jszgh')
            if len(str(jszgh)) > 6:
                id = str(x.get("_id"))
                x['jszgh'] = str(jszgh)[0:6]
                self.baseRepository.update_by_id(id, x)
                print(x)

        print(num)
        print(msg)

    def test_replace_JSZGH_into_Str(self):
        from logic.jwxt.TeachTask import TeachTaskLogic
        from model.logic.Score import Score
        sl = TeachTaskLogic()
        from repository.BaseRepository import BaseRepository
        self.collectionName = str(Score().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)
        result, num, msg = self.baseRepository.get_all_no_page()
        for x in result:
            x = dict(x)
            jszgh = x.get('jszgh')
            id = str(x.get("_id"))
            if len(str(jszgh)) > 6:
                x['jszgh'] = str(jszgh).strip()[0:6]
                self.baseRepository.update_by_id(id, x)
                print(x)
            else:
                x['jszgh'] = str(jszgh).strip()
                self.baseRepository.update_by_id(id, x)
        print(num)
        print(msg)


if __name__ == '__main__':
    unittest.main(2)
