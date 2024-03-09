from Src.Logics.reports.converter import *
from Src.Logics.reports.converter.convertor import convertor
from Src.Models import abstract_referance
from Utils import typecheck
from datetime import datetime

class convert_factory:
    
    @staticmethod
    def create(obj):
        if isinstance(obj, abstract_referance):
            return convertor_modelss
        elif isinstance(obj, datetime):
            return convertor_datetime
        else:
            return convertor_basic


class convertor_modelss(convertor):

    @staticmethod
    @typecheck
    def convert(obj: abstract_referance):
        return {key:convert_factory.create(value).convert(value) for key, value in obj.get_by_attr('head').items()}


        