from Src.Logics.reports.converter import *
from functools import singledispatch
from datetime import datetime
from Utils import AttrWorker
from Src.Models import *

class convert_factory:
    
    @singledispatch
    @staticmethod
    def create(obj):
        return convertor_basic


    @create.register
    def create_model(obj: AttrWorker):
        return convertor_models


    @create.register
    def create_datetime(obj: datetime):
        return convertor_datetime


    @create.register
    def create_iterator(obj: list):
        return convertor_iterator
