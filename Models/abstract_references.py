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
    @typecheck
    def name(self, value: str):
        self.__name = value.strip()


    @property
    def error(self):
        return self.__error


class unit(abstract_referance):
    '''
    Единица измерения, надо чтоб были уникальные по названию
    '''
    __base = None
    __num : int

    def __init__(self, base: "unit" = None, num: int = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__base = base
        self.__num = num


    @property
    def num(self):
        return self.__num


    @num.setter
    @typecheck
    def num(self, value: int):
        self.__num = value


    @property
    def base(self):
        return self.__base


    def __str__(self):
        return f"{self.num} {self.name}"


    