from Src.exeptions import operation_exception, argument_exception
from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.reports.converter import convert_factory
from Src.Logics.processes import process_factory
from functools import singledispatchmethod
from Src.Storage.storage import storage
from Src.Models import period
from Utils import typecheck
from typing import Union
from Src.Models import *
import json


class storage_service:
    __data = []


    @typecheck
    def __init__(self, data: list):
        self.__data = data


    @singledispatchmethod
    def create_turns(self, obj, **kwargs):
        raise operation_exception(f"Нет сервиса для {type(obj)}.")


    @create_turns.register
    def _(self, obj: period, **kwargs):
        prototype = storage_prototype( self.__data )
        transactions = prototype.filter_by( obj ).data
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)
        return rests


    @create_turns.register
    def _(self, obj: nomen_model, **kwargs):
        prototype = storage_prototype( self.__data )
        transactions = prototype.filter_by( obj ).data
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)
        return rests


    @create_turns.register
    def _(self, obj: recipe_model, **kwargs):
        if 'storage' not in kwargs.keys(): raise argument_exception("Для создания оборотов по рецепту, нужно передать склад!")
        prototype = storage_prototype( self.__data )
        transactions = prototype.filter_by( kwargs['storage'] ).filter_by( obj ).data
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)
        return rests

    
    @staticmethod
    def create_response(data: list | dict, app):
        data = convert_factory.create(data).convert(data)
        data = json.dumps(data, indent=4, ensure_ascii=False)

        result = app.response_class(
            response = data,
            status=200,
            mimetype="application/json; charset=utf-8"
        )
        return result


    @property
    def data(self) -> list:
        return self.__data