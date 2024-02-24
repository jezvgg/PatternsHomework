from Src.Models.abstract_references import abstract_referance
from Utils.typecheck import typecheck
from Models import *


class recipe_model(abstract_referance):
    __nomenculatures: nomen_model = None
    __size: int = 0
    __unit: unit_model = None


    @typecheck
    def __init__(self, nomenculature: nomen_model, size: int, unit: unit_model):
        self.__nomenculatures = nomenculature
        self.__size = size
        self.__unit = unit

        super().__init__(f"{self.__nomenculatures.name}, {self.__unit.name}")


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