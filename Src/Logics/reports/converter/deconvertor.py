import json
from Src.Models import *
from Utils import typecheck
from functools import singledispatchmethod
import datetime


class deconvertor:

    @typecheck
    def load(self, src: str, dtype: type):
        with open(src) as f:
            res = json.load(f)
        return self.deserialize(res, dtype)


    @singledispatchmethod
    def deserialize(self, obj, obj_type: type):
        return obj


    @deserialize.register
    def deserialize_obj(self, obj: dict, obj_type: type):
        if isinstance(obj_type, str): obj_type = eval(obj_type)
        print('_')
        print(obj_type, obj)
        print({value.fget.__name__:self.deserialize(value, value.fget.__annotations__['return']) for key, value in obj_type.get_by_attr('head').items()})
        return obj_type(**{value.fget.__name__:self.deserialize(obj[key], value.fget.__annotations__['return']) for key, value in obj_type.get_by_attr('head').items()})


    @deserialize.register
    def deserialize_list(self, obj: list, obj_type: type):
        print('-')
        