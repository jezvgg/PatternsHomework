from Src.Models import *
from Src.settings import Settings
from Src.Storage.storage import storage
from Src.Logics.services import storage_service, post_processing_service, logging_service
from Src.Logics.observer import observer
from Src.Logics.event_type import event_type
from datetime import datetime
from Utils import *


class start_factory:
    __options: Settings = None
    __storage: storage = None


    @typecheck
    def __init__(self, options: Settings, storage_: storage | None = None):
        self.__options = options
        self.__storage = storage_
        self.__build()


    def __build(self):
        '''
            Сформулировать данные в словаре
        '''
        if not self.__storage:
            self.__storage = storage()

        nomens = start_factory.create_nomenculature()
        recepts = start_factory.create_recipets()
        journal = start_factory.create_journal()
        storages = start_factory.create_storages()

        st_service = storage_service(journal)
        post_service = post_processing_service( recepts )
        logs = []
        log_service = logging_service( logs )
    
        observer.raise_event(event_type.create_log())
        self.__storage.data[storage.log_key()] = logs
        self.__storage.data[storage.nomenculature_key()] = nomens
        self.__storage.data[storage.unit_key()] = list(set([x.units for x in nomens]))
        self.__storage.data[storage.group_key()] = list(set([x.group for x in nomens]))
        self.__storage.data[storage.recipe_key()] = recepts
        self.__storage.data[storage.journal_key()] = journal
        self.__storage.data[storage.storages_key()] = storages
        st_service.create_blocked_turns()



    @property
    def storage(self):
        return self.__storage


    def create(self) -> list:
        if not self.__storage: self.__build()

        self.__options.is_first_start = False
        result = list(self.__storage.data.values())
            
        return result

    
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
        nomen_model(name='Оливковое масло', group=nomen_group, units=unit_model.create_litres()),
        nomen_model(name='Лимонный сок', group=nomen_group, units=unit_model.create_litres()),
        nomen_model(name='Горчица дижонская', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Яичный белок', group=nomen_group, units=unit_model.create_count()),
        nomen_model(name='Сахарная пудла', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Корица', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Какао', group=nomen_group, units=unit_model.create_gramm())
        ]


    @staticmethod
    def create_recipets():
        return [
            recipe_model(
                name='ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ',
            rows=[recipe_row_model(
                nomenculature = nomen_model(name='Пшеничная мука', group=nomen_group_model.create_group(), units=unit_model.create_kilogramm()),
                unit=unit_model.create_gramm(),
                size=100
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Сахар', group=nomen_group_model.create_group(), units=unit_model.create_kilogramm()),
                unit=unit_model.create_gramm(),
                size=80
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Сливочное масло', group=nomen_group_model.create_group(), units=unit_model.create_gramm()),
                unit=unit_model.create_gramm(),
                size=70
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Яйца', group=nomen_group_model.create_group(), units=unit_model.create_count()),
                unit=unit_model.create_count(),
                size=1
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Ванилин', group=nomen_group_model.create_group(), units=unit_model.create_gramm()),
                unit=unit_model.create_gramm(),
                size=5
                )],
            description='''
            Время приготовления: 20 мин

Как испечь вафли хрустящие в вафельнице? Подготовьте необходимые продукты. Из данного количества у меня получилось 8 штук диаметром около 10 см.
Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо в микроволновке.
Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар довольно быстро растает.
Добавьте в масло яйцо. Предварительно все-таки проверьте масло, не горячее ли оно, иначе яйцо может свариться. Перемешайте яйцо с маслом до однородности.
Всыпьте муку, добавьте ванилин.
Перемешайте массу венчиком до состояния гладкого однородного теста.
Разогрейте вафельницу по инструкции к ней. У меня очень старая, еще советских времен электровафельница. Она может и не очень красивая, но печет замечательно! Я не смазываю вафельницу маслом, в тесте достаточно жира, да и к ней уже давно ничего не прилипает. Но вы смотрите по своей модели. Выкладывайте тесто по столовой ложке. Можно класть немного меньше теста, тогда вафли будут меньше и их получится больше.
Пеките вафли несколько минут до золотистого цвета. Осторожно откройте вафельницу, она очень горячая! Снимите вафлю лопаткой. Горячая она очень мягкая, как блинчик. Но по мере остывания становится твердой и хрустящей. Такие вафли можно свернуть трубочкой. Но делать это надо сразу же после выпекания, пока она мягкая и горячая, потом у вас ничего не получится, вафля поломается. Приятного аппетита!
            ''')
        ]

    @staticmethod
    def create_journal():
        storage = storage_model(name='Главный склад', adress='ул. Пушкина, д. Колотушкина, 23')
        storage2 = storage_model(name='Не главный склад', adress='ул. Не Пушкина, д. Не Колотушкина, не 23')

        nomen_group = nomen_group_model.create_group()

        unit = unit_model.create_count()
        kilogram = unit_model.create_kilogramm()
        gramm = unit_model.create_gramm()

        nomen1 = nomen_model(name='Яйца', group=nomen_group, units=unit)
        nomen2 = nomen_model(name='Сахар', group=nomen_group, units=kilogram)
        nomen3 = nomen_model(name='Сливочное масло', group=nomen_group, units=gramm)
        nomen4 = nomen_model(name='Пшеничная мука', group=nomen_group, units=kilogram)
        nomen5 = nomen_model(name='Ванилин', group=nomen_group, units=gramm)

        return [
            storage_transaction_model(storage=storage, nomen=nomen1, operation=True,
                                                countes=200, unit=unit, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen1, operation=False,
                                                countes=50, unit=unit, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen1, operation=False,
                                                countes=100, unit=unit, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen2, operation=True,
                                                countes=200, unit=kilogram, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen2, operation=True,
                                                countes=50, unit=kilogram, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen2, operation=False,
                                                countes=150, unit=kilogram, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen3, operation=True,
                                                countes=23000, unit=gramm, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen3, operation=False,
                                                countes=23000, unit=gramm, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen1, operation=True,
                                                countes=200, unit=unit, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen1, operation=False,
                                                countes=50, unit=unit, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen1, operation=False,
                                                countes=100, unit=unit, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen2, operation=True,
                                                countes=200, unit=kilogram, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen2, operation=True,
                                                countes=50, unit=kilogram, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen2, operation=False,
                                                countes=150, unit=kilogram, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen3, operation=True,
                                                countes=23000, unit=gramm, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen3, operation=False,
                                                countes=23000, unit=gramm, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen1, operation=True,
                                                countes=200, unit=unit, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen1, operation=False,
                                                countes=50, unit=unit, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen1, operation=False,
                                                countes=100, unit=unit, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen2, operation=True,
                                                countes=200, unit=kilogram, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen2, operation=True,
                                                countes=50, unit=kilogram, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen2, operation=False,
                                                countes=150, unit=kilogram, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen3, operation=True,
                                                countes=23000, unit=gramm, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen3, operation=False,
                                                countes=23000, unit=gramm, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen4, operation=True,
                                                countes=23000, unit=gramm, period=datetime.now()),
            storage_transaction_model(storage=storage, nomen=nomen3, operation=True,
                                                countes=100, unit=gramm, period=datetime.now())                               
        ]


    @staticmethod
    def create_storages():
        storage = storage_model(name='Главный склад', adress='ул. Пушкина, д. Колотушкина, 23')
        storage2 = storage_model(name='Не главный склад', adress='ул. Не Пушкина, д. Не Колотушкина, не 23')
        return [storage, storage2]
