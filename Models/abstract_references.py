import uuid
from abc import ABC
from Src.error_proxy import error_proxy
from Utils.typecheck import typecheck


class abstract_referance(ABC):
    __id: uuid.UUID
    __name: str = ''
    __error: error_proxy = error_proxy()


    def __init__(self, name: str = None):
        self.name = name
        self.__id = uuid.uuid4()

    @property
    def name(self):
        return self.__name.strip()


    @name.setter
    @typecheck(expression = lambda x: len(x['value']) < 50)
    def name(self, value: str):
        self.__name = value.strip()


    @property
    def error(self):
        return self.__error
    