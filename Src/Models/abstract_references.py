import uuid
from Utils import *


class abstract_referance(AttrWorker):
    __id: uuid.UUID
    __name: str = ''


    @typecheck
    def __init__(self, name: str = '', id: str = ''):
        super().__init__()
        self.name = name
        self.__id = id
        if not id: self.__id = str(uuid.uuid4())


    def __new__(cls, name: str, *args, **kwargs):
        if not hasattr(cls, str(hash(name))):
            setattr( cls, str(hash(name)), super(abstract_referance, cls).__new__(cls))
        return getattr(cls, str(hash(name)))


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


    @attribute(head='Код')
    def id(self) -> str:
        return self.__id


    
    