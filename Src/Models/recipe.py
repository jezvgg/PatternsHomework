from Src.Models.abstract_references import abstract_referance
from Utils import typecheck, attribute, AttrWorker
from Src.Models import *
import uuid


class recipe_row_model(AttrWorker):
    __nomenculatures: nomen_model = None
    __size: int = 0
    __unit: unit_model = None


    @typecheck
    def __init__(self, nomenculature: nomen_model, size: int, unit: unit_model):
        self.__nomenculatures = nomenculature
        self.__size = size
        self.__unit = unit


    @attribute(head='Номенкулятура')
    def nomenculature(self) -> nomen_model:
        return self.__nomenculatures


    @attribute(head='Объём')
    def size(self) -> int:
        return self.__size


    @size.setter
    @typecheck
    def size(self, value : int):
        self.__size = value

    
    @attribute(head='Единицы измерения')
    def unit(self) -> unit_model:
        return self.__unit


class recipe_model(abstract_referance):
    __rows: list[recipe_row_model]
    __description: str


    @typecheck
    def __init__(self, name: str, rows: list[recipe_row_model], description: str = '', id: str = str(uuid.uuid4())):
        self.__rows = rows
        self.description = description
        super().__init__(name)


    @attribute(head='Рецепт')
    def rows(self) -> list[recipe_row_model]:
        return self.__rows


    @attribute(head='Описание')
    def description(self) -> str:
        return self.__description


    @description.setter
    @typecheck(expression=lambda x: x['value'])
    def description(self, value: str):
        self.__description = value