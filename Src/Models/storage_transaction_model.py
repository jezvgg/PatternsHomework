from Src.Models import abstract_referance
from Src.Models import *
from Utils import typecheck, attribute
from datetime import datetime


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
                unit: unit_model, period: datetime,  name: str | None = None):
        super().__init__(name)
        self.__storage = storage
        self.__nomen = nomen
        self.__operation = operation
        self.__contes = countes
        self.__unit = unit
        self.__period = period

    
    @property
    def name(self):
        return self.name

    
    @name.setter
    def name(self, value):
        self.__name = value

    
    @attribute(head='Склад')
    def storage(self):
        return self.__storage


    @attribute(head='Номенкулатура')
    def nomenculature(self):
        return self.__nomen


    @attribute(head='Операция')
    def opearation(self):
        return self.__operation


    @attribute(head='Количество')
    def counts(self):
        return self.__contes


    @attribute(head='Единицы измерения')
    def unit(self):
        return self.__unit


    @attribute(head='Период')
    def period(self):
        return self.__period