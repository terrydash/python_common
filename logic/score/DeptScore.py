class DeptScoreLogic:
    def dept_reply(self, id: str, reply_content: str):
        from logic.score.Score import ScoreLogic
        sl = ScoreLogic()
        print(id, reply_content)
        result, num, msg = sl.baseRepository.get_by_id(id)
        if result is not None:
            replyentity = {'is_dept_reply': 1, 'dept_manager_reply': str(reply_content)}
            result, num, msg = sl.baseRepository.update_by_id(_id=id, entity=replyentity)
            return result, num, msg;
        return None, 0, 'id不正确'
