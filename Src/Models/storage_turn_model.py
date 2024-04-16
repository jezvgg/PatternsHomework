from Src.Models import abstract_referance
from Utils import typecheck, attribute
from Src.Models import *


class storage_turn_model(abstract_referance):
    __storage: storage_model
    __remains: int
    __nomen: nomen_model
    __unit: unit_model


    @typecheck
    def __init__(self, storage_: storage_model, remains: int,
                nomen: nomen_model, unit: unit_model, name: str = ''):
        super().__init__(name)
        self.__storage = storage_
        self.__remains = remains
        self.__nomen = nomen
        self.__unit = unit


    @attribute(head='Склад')
    def storage(self) -> storage_model:
        return self.__storage


    @attribute(head='Оборот')
    def remains(self) -> int:
        return self.__remains


    @attribute(head='Номенкулятура')
    def nomen(self) -> nomen_model:
        return self.__nomen


    @attribute(head='Единицы измерения')
    def unit(self) -> unit_model:
        return self.__unit