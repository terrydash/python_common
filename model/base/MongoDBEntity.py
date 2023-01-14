import sys


class MongoDBEntity(object):
    _COLLECTION_NAME = ''

    def __init__(self):
        self._COLLECTION_NAME = self.__class__.__name__.lower()

    def __COLLECTION_NAME__(self):
        if len(self._COLLECTION_NAME) == 0:
            self._COLLECTION_NAME = self.__class__.__name__.lower()
        return self._COLLECTION_NAME

    @property
    def COLLECTION_NAME(self):
        return self._COLLECTION_NAME
