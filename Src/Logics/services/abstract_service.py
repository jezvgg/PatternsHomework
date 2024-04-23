import json
from abc import ABC
from Utils import typecheck
from Src.Logics.reports.converter import convert_factory


class abstract_service(ABC):
    _data = []


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


    @typecheck
    def __init__(self, data: list):
        self._data = data


    @property
    def data(self) -> list:
        return self._data