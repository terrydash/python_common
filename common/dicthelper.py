class dictHelper(object):
    def __init__(self, indict: dict = None):
        self.dict = self.remove_space(indict)

    def remove_space(self, indict: dict):
        if indict is None:
            raise Exception("dict should not be none!")
        for k in indict.keys():
            if isinstance(indict[k], str):
                indict[k] = str(indict[k]).strip()
            if isinstance(indict[k], dict):
                indict[k] = self.remove_space(indict[k])
        return indict

    def check_keys(self, key_list: list):
        not_in_keyname_list = []
        for keyname in key_list:
            if keyname not in self.dict or (
                    keyname in self.dict and self.dict[keyname] is None):
                not_in_keyname_list.append(keyname)
            else:
                if not self.check_value_is_not_empty(keyname):
                    not_in_keyname_list.append(keyname)
        print(not_in_keyname_list)
        if len(not_in_keyname_list) == 0:
            return True, []
        else:
            return False, not_in_keyname_list

    def check_value_is_not_empty(self, keyname):
        if isinstance(self.dict[keyname], str) or isinstance(self.dict[keyname], list):
            return len(self.dict[keyname]) > 0
        if isinstance(self.dict[keyname], int):
            return self.dict[keyname] is not None
        if isinstance(self.dict[keyname], dict):
            return self.dict[keyname].keys() > 0
        raise Exception('不支持的数据类型')
