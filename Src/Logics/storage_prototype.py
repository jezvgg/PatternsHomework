from Utils import typecheck
from functools import singledispatchmethod
from Src.exeptions import operation_exception
from Src.Models import *


class storage_prototype:
    __data: list[storage_transaction_model] = []


    @typecheck
    def __init__(self, data: list[storage_transaction_model]):
        self.__data = data


    @singledispatchmethod
    def filter_by(self, filter_model):
        raise operation_exception(f"Нет фильтрации такого способа: {type(filter_model)}")


    @filter_by.register
    def filter_by_period(self, filter_model: period):
        result = []
        for item in self.data:
            if item.period > filter_model.start and item.period <= filter_model.end:
                result.append(item)

        return storage_prototype(result)


    @filter_by.register
    def filter_by_nomen(self, filter_model: nomen_model):
        result = []
        for item in self.data:
            if item.nomenculature.name != filter_model.name: continue
            result.append(item)
        return storage_prototype(result)


    @filter_by.register
    def filter_by_recipe(self, filter_model: recipe_model):
        recipe_nomens = set([row.nomenculature.name for row in filter_model.rows])
        result = []
        for item in self.data:
            if item.nomenculature.name not in recipe_nomens: continue
            result.append(item)
        return storage_prototype(result)


    @filter_by.register
    def filter_by_recipe(self, filter_model: storage_model):
        result = []
        for item in self.data:
            if item.storage.name != filter_model.name: continue
            result.append(item)
        return storage_prototype(result)


    @property
    def data(self) -> list[storage_transaction_model]:
        return self.__data

