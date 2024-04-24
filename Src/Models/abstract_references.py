import uuid
from abc import ABC
from Src.error_proxy import error_proxy
from Utils import attribute, typecheck, AttrWorker


class abstract_referance(ABC, AttrWorker):
    __id: uuid.UUID
    __name: str = ''
    __error: error_proxy = error_proxy()


    @typecheck
    def __init__(self, name: str = '', id: str = ''):
        super().__init__()
        self.name = name
        self.__id = id
        if not id: self.__id = str(uuid.uuid4())

    def __str__(self) -> None:
        return str(self.id)


    def __repr__(self) -> None:
        return f"{type(self).__name__}({', '.join([f'{key}={value}' for key, value in self.get_by_attr('head').items()])})"

    
    def __hash__(self) -> int:
        return hash(self.name)


    @attribute(head='Название')
    def name(self) -> str:
        return self.__name.strip()


    @name.setter
    @typecheck
    def name(self, value: str, id: str = ''):
        self.__name = value.strip()


    @property
    def _error(self):
        return self.__error


    @attribute(head='Код')
    def id(self) -> str:
        return self.__id


    
    