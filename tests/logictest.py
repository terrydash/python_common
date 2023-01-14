import unittest

from config.startupconfig import init_config
from logic.JWXTStudent import getXsjbxx


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        self.config = init_config

    # 销毁
    def tearDown(self):
        pass

    # 具体的测试用例，以test开头
    def testjwxt(self):
        stu = getXsjbxx('1702020105');

        self.assertIsNotNone(stu, '测试成功!')

    def test_updatetotalscore(self):
        pass
        from logic.score.Score import ScoreLogic
        sl = ScoreLogic()
        result, msg, num = sl.get_all_fromdb()
        for score in result:
            if score['result'] is not None and len(score['result']) > 0:
                sum = 0
                for element in score['result']:
                    fi: dict = element['fi']
                    si: dict = element['si']
                    sum = sum + int(fi.get('proportion')) * int(si.get('value')) / 100
                score['totalscore'] = int(sum)
            sl.baseRepository.update_by_id(_id=str(score['_id']), entity=score)
        print(result)

    def test_insertSecondIndex(self):
        from model.logic.SecondIndex import SecondIndex
        from logic.course_evaluate.SecondIndex import SecondIndexLogic
        from logic.course_evaluate.FirstIndex import FirstIndexLogic
        fis, num, msg = FirstIndexLogic().search_no_page('', '5b7482e9d72e2316cc2bf3c2', None)
        sil = SecondIndexLogic()
        for x in fis:
            fiid = str(x.get('_id'))
            scid = str(x.get('courseEvaluate').get('_id'))
            si = SecondIndex()
            si.courseEvaluateID = scid
            si.firstIndexID = fiid
            si.description = ''
            si.height = 100
            si.is_department_can_reply = True
            si.is_department_can_see = True
            si.is_teacher_can_reply = True
            si.is_teacher_can_see = True
            si.remarks = ''
            si.scheme_type = 2
            si.result = ''
            si.width = 100

            si.name = "优秀"
            si.order = 1
            si.value = 100
            sil.insert(si)
            si.name = "良好"
            si.order = 2
            si.value = 80
            sil.insert(si)
            si.name = "合格"
            si.order = 3
            si.value = 60
            sil.insert(si)
            si.name = "不合格"
            si.order = 4
            si.value = 40
            sil.insert(si)


if __name__ == '__main__':
    unittest.main(2)
