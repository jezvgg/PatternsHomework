import json
from Src.Models import *
from Utils import typecheck
from functools import singledispatch


class deconvertor:

    @staticmethod
    @typecheck
    def load(url: str):
        pass


    @staticmethod
    @singledispatch
    def desirialize(obj: dict, obj_type):
        pass