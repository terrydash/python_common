class TeacherScoreLogic:
    def teacher_reply(self, id: str, reply_content: str):
        from logic.score.Score import ScoreLogic
        sl = ScoreLogic()
        print(id,reply_content)

        result, num, msg = sl.baseRepository.get_by_id(id)
        if result is not None :
            replyentity = {'is_teacher_reply': 1, 'teacher_reply': str(reply_content)}
            result, num, msg= sl.baseRepository.update_by_id(_id=id, entity=replyentity)
            return result, num, msg;
        return None, 0, 'id不正确'

    def judge_supervision(self, id: str, reply_result: str):
        from logic.score.Score import ScoreLogic
        sl = ScoreLogic()
        print(id,reply_result)
        result, num, msg = sl.baseRepository.get_by_id(id)
        if result is not None :
            replyentity = {'is_teacher_judge_supervison': 1, 'teacher_judge_supervison_result': str(reply_result)}
            result, num, msg= sl.baseRepository.update_by_id(_id=id, entity=replyentity)
            return result, num, msg;
        return None, 0, 'id不正确'