from Src.Logics.prototypes import abstract_prototype
from Src.exeptions import operation_exception
from functools import singledispatchmethod
from Src.Models import *
import uuid


class nomenculature_prototype(abstract_prototype):

    @singledispatchmethod
    def filter_by(self, filter_model):
        raise operation_exception(f"Нет фильтрации такого способа: {type(filter_model)}")

    
    @filter_by.register
    def filter_by_id(self, filter_model: uuid.UUID):
        return [nomen for nomen in self._data if nomen.id == str(filter_model)]
