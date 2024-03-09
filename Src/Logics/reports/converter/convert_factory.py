from Src.Logics.reports.converter import *
from datetime import datetime
from Src.Models import *

class convert_factory:
    
    @staticmethod
    def create(obj):
        if isinstance(obj, abstract_referance):
            return convertor_modelss
        elif isinstance(obj, datetime):
            return convertor_datetime
        else:
            return convertor_basic
