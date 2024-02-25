from Src.Models.abstract_references import abstract_referance
from Src.exeptions import argument_exception
from functools import singledispatch
from Utils.typecheck import typecheck
from pathlib import Path
from Src.Models import *


class recipe_row_model(abstract_referance):
    __nomenculatures: nomen_model = None
    __size: int = 0
    __unit: unit_model = None


    @typecheck
    def __init__(self, nomenculature: nomen_model, size: int, unit: unit_model):
        self.__nomenculatures = nomenculature
        self.__size = size
        self.__unit = unit

        super().__init__(name=f"{self.__nomenculatures.name}, {size} {self.__unit.name}")


    @property
    def nomenculature(self):
        return self.__nomenculatures


    @property
    def size(self):
        return self.__size


    @size.setter
    @typecheck
    def size(self, value : int):
        self.__size = value

    
    @property
    def unit(self):
        return self.__unit


class recipe_model(abstract_referance):
    __rows: list
    __description: str


    @typecheck
    def __init__(self, name: str, rows: list[recipe_row_model], description: str = ''):
        self.__rows = rows
        self.description = description
        super().__init__(name)


    @property
    def description(self):
        return self.__description


    @description.setter
    @typecheck(expression=lambda x: x['value'])
    def description(self, value: str):
        self.__description = value