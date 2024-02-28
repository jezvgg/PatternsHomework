import uuid
from abc import ABC
from Src.error_proxy import error_proxy
from Utils.typecheck import typecheck
from Utils.header import header


class abstract_referance(ABC):
    __id: uuid.UUID
    __name: str = ''
    __error: error_proxy = error_proxy()


    def __init__(self, name: str = None):
        self.name = name
        self.__id = str(uuid.uuid4())

    @property
    @header(name='Название')
    def name(self):
        return self.__name.strip()


    @name.setter
    @typecheck
    def name(self, value: str):
        self.__name = value.strip()


    @property
    def _error(self):
        return self.__error


    @property
    @header
    def id(self):
        return self.__id
    