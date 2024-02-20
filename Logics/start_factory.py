from Models import *
from Src.settings import Settings


class start_factory:
    __options: Settings = None


    def __init__(self, options: Settings) -> None:
        self.__options = options


    def create(self):
        if self.__options.is_first_start:
            self.__options.is_first_start = False
            return start_factory.create_nomenculature()
        return []

    
    @staticmethod
    def create_nomenculature():
        nomen_group = nomen_group_model.create_group()
        nomen1 = nomen_model(name='Пшеничная мука', full_name='Пшеничная мука', group=nomen_group, units=unit_model.create_kilogramm())
        nomen2 = nomen_model(name='Сахар', full_name='Сахар', group=nomen_group, units=unit_model.create_kilogramm())
        nomen3 = nomen_model(name='Сливочное масло', full_name='Сливочное масло', group=nomen_group, units=unit_model.create_gramm())
        nomen4 = nomen_model(name='Яйца', full_name='Яйца', group=nomen_group, units=unit_model.create_count())
        nomen5 = nomen_model(name='Ванилин', full_name='Ванилин', group=nomen_group, units=unit_model.create_gramm())
        return [nomen1,nomen2,nomen3,nomen4,nomen5]
