from Src.Logics.reports.converter import convertor
from Src.exeptions import argument_exception
from Utils import typecheck
import json


class convertor_basic(convertor):

    @staticmethod
    @typecheck
    def convert(obj):
        try:
            json.dumps(obj)
        except TypeError:
            raise argument_exception("Not standart type to serialize!")

  #      if obj is None: obj = str(obj)

        return obj
