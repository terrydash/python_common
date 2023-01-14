class BaseLogic:
    def get_all_page(self, page, pagesize, sort):
        result, num, msg = self.baseRepository.get_all_page(page, pagesize, sort)
        return result, num, msg

    def get_all_fromdb(self):
        result, num, msg = self.baseRepository.get_all_no_page()
        return result, num, msg

    def get_by_id(self, _id):
        result, num, msg = self.baseRepository.get_by_id(_id)
        return result, num, msg

    def search_no_page(self, query=None, sort=None):
        result, num, msg = self.baseRepository.search_no_page(query, sort)
        return result, num, msg

    def delete_all(self,query={}):
        result, num, msg = self.baseRepository.delete_all(query=query)
        return result, num, msg
