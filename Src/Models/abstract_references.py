import uuid
from abc import ABC
from Src.error_proxy import error_proxy
from Utils import attribute, typecheck, AttrWorker


class abstract_referance(ABC, AttrWorker):
    __id: uuid.UUID
    __name: str = ''
    __error: error_proxy = error_proxy()


    @typecheck
    def __init__(self, name: str = ''):
        self.name = name
        self.__id = str(uuid.uuid4())


    def __str__(self):
        return str(self.id)


    def __repr__(self):
        return f"{type(self).__name__}({', '.join([f'{key}={value}' for key, value in self.get_by_attr('head').items()])})"

    
    def __hash__(self) -> int:
        return hash(self.name)


    @attribute(head='Название')
    def name(self):
        return self.__name.strip()


    @name.setter
    @typecheck
    def name(self, value: str):
        self.__name = value.strip()


    @property
    def _error(self):
        return self.__error


    @attribute(head='Код')
    def id(self):
        return self.__id


    
    