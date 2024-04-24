import json
from Src.Models import *
from Utils import typecheck
import datetime
from types import GenericAlias


class deconvertor:
    convertor_factory: dict


    def __init__(self):
        self.convertor_factory = {str: self.deserialize_basic,
                                    int: self.deserialize_basic,
                                    GenericAlias: self.deserialize_list,
                                    datetime.datetime: self.deserialize_datetime,
                                    bool: self.deserialize_basic}

    @typecheck
    def load(self, src: str, dtype: type | GenericAlias):
        with open(src) as f:
            res = json.load(f)
        return self.deserialize(res, dtype)


    def deserialize(self, obj, obj_type: type):
        if hasattr(obj_type, '__origin__'):
            convertor = self.deserialize_list
        elif obj_type not in self.convertor_factory.keys():
            convertor = self.deserialize_obj
        else: convertor = self.convertor_factory[obj_type]
        return convertor(obj, obj_type)


    def deserialize_basic(self, obj, obj_type):
        return obj


    def deserialize_obj(self, obj: dict, obj_type: type):
        if isinstance(obj_type, str): obj_type = eval(obj_type)
        if not obj: return None
        res = {}
        for key, value in obj_type.get_by_attr(obj_type, 'head').items():
            res[value.fget.__name__] = self.deserialize(obj[key], value.fget.__annotations__['return'])
        return obj_type(**{value.fget.__name__:self.deserialize(obj[key], value.fget.__annotations__['return']) for key, value in obj_type.get_by_attr(obj_type, 'head').items()})


    def deserialize_datetime(self, obj: datetime.datetime, obj_type: type):
        return datetime.datetime(obj['Год'], obj['Месяц'], obj['День'], obj['Час'], obj['Минуты'], obj['Секунды'])


    def deserialize_list(self, obj: list, obj_type: type):
        return [self.deserialize(objj, obj_type.__args__[0]) for objj in obj]
        