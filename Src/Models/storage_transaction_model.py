from Src.Models import abstract_referance
from Utils import typecheck, attribute
from datetime import datetime
from Src.Models import *


class storage_transaction_model(abstract_referance):
    __storage: storage_model
    __nomen: nomen_model
    __operation: bool
    __contes: int
    __unit: unit_model
    __period: datetime


    @typecheck
    def __init__(self, storage: storage_model, 
                nomen: nomen_model, operation: bool, countes: int, 
                unit: unit_model, period: datetime,  name: str = ''):
        super().__init__()
        self.__name = name
        self.__storage = storage
        self.__nomen = nomen
        self.__operation = operation
        self.__contes = countes
        self.__unit = unit
        self.__period = period

    
    @property
    def name(self) -> str:
        return self.__name

    
    @name.setter
    def name(self, value):
        self.__name = value

    
    @attribute(head='Склад')
    def storage(self) -> storage_model:
        return self.__storage


    @attribute(head='Номенкулатура')
    def nomenculature(self) -> nomen_model:
        return self.__nomen


    @attribute(head='Операция')
    def opearation(self) -> bool:
        return self.__operation


    @attribute(head='Количество')
    def counts(self) -> int:
        return self.__contes


    @attribute(head='Единицы измерения')
    def unit(self) -> unit_model:
        return self.__unit


    @attribute(head='Период')
    def period(self):
        return self.__period