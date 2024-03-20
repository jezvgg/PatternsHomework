from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.reports.converter import convert_factory
from Src.Logics.processes import process_factory
from Src.Storage.storage import storage
from Src.Models import period
from Utils import typecheck
import json


class storage_service:
    __data = []


    @typecheck
    def __init__(self, data: list):
        self.__data = data


    @typecheck
    def create_turns(self, dates: period):
        prototype = storage_prototype( self.__data )
        transactions = prototype.filter_by( dates ).data
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