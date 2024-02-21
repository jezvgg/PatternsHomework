from Models import *
from Src.settings import Settings
from Storage.storage import storage


class start_factory:
    __options: Settings = None
    __storage: storage = None


    def __init__(self, options: Settings, storage_: storage = None) -> None:
        self.__options = options
        self.__storage = storage_
        self.__build()


    def __build(self):
        '''
            Сформулировать данные в словаре
        '''
        if not self.__storage:
            self.__storage = storage()

        self.__storage.data[storage.nomenculature_key] = start_factory.create_nomenculature()
        self.__storage.data[storage.unit_key] = set([x.units for x in start_factory.create_nomenculature()])
        self.__storage.data[storage.group_key] = set([x.group for x in start_factory.create_nomenculature()])


    @property
    def storage(self):
        return self.__storage


    def create(self):
        if self.__options.is_first_start:
            self.__options.is_first_start = False
            return start_factory.create_nomenculature()
        return []

    
    @staticmethod
    def create_nomenculature():
        nomen_group = nomen_group_model.create_group()
        return [
        nomen_model(name='Пшеничная мука', full_name='Пшеничная мука', group=nomen_group, units=unit_model.create_kilogramm()),
        nomen_model(name='Сахар', full_name='Сахар', group=nomen_group, units=unit_model.create_kilogramm()),
        nomen_model(name='Сливочное масло', full_name='Сливочное масло', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Яйца', full_name='Яйца', group=nomen_group, units=unit_model.create_count()),
        nomen_model(name='Ванилин', full_name='Ванилин', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Куриное филе', group=nomen_group, units=unit_model.create_kilogramm()),
        nomen_model(name='Салат Романо', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Сыр Пармезан', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Чеснок', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Белый хлеб', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Соль', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Чёрный перец', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Оливковое масло', group=nomen_group, units=unit_model.create_milolitres()),
        nomen_model(name='Лимонный сок', group=nomen_group, units=unit_model.create_milolitres()),
        nomen_model(name='Горчица дижонская', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Яичный белок', group=nomen_group, units=unit_model.create_count()),
        nomen_model(name='Сахарная пудла', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Корица', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Какао', group=nomen_group, units=unit_model.create_gramm())
        ]
