from Src.Logics.reports.converter import convertor
from Src.exeptions import argument_exception
import json


class convertor_basic(convertor):

    @staticmethod
    def convert(obj):
        try:
            json.dumps(obj)
        except TypeError:
            raise argument_exception(f"{obj} - Not standart type to serialize!")

        return obj
