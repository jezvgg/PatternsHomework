from Src.settings_manager import settings_manager
from datetime import datetime
from pathlib import Path
from Src.Models import *
import unittest


class test_models(unittest.TestCase):

    def test_unit(self):
        units = unit_model(name='gram')

        assert units.name == 'gram'

    def test_big_unit(self):
        gram = unit_model(name='gram')
        kilogram = unit_model(base=gram, coef=1000, name='kilogram')

        gram_in_kilo = kilogram.to_base

        assert gram_in_kilo.name == 'gram'
        assert gram_in_kilo.base == None


    def test_biggest_unit(self):
        bit = unit_model(name='bit')
        bite = unit_model(name='bite', base=bit, coef=8)
        kilobite = unit_model(name='kilobite', base=bite, coef=1024)

        assert kilobite.to_base.name == 'bit'

    def test_organizations(self):
        manager = settings_manager()
        manager.open('settings.json')
        organ = organization_model(settings=manager.settings, name='org')

        assert all(filter(lambda x: x.startswith('_'), dir(organ)))

    def test_nomen_group(self):
        group = nomen_group_model(name='Group one')

        assert bool(group) == True

    def test_nomen(self):
        nom = nomen_model(name="nomen1", group = nomen_group_model('Group'), units=unit_model(name='unit'))

        assert bool(nom) == True

    def test_recipe_row(self):
        row = recipe_row_model(nomenculature=nomen_model(name="nomen1", group = nomen_group_model(name='Group'), units=unit_model(name='unit')),
        size=200, unit=unit_model.create_gramm())

        assert bool(row) == True

    def test_recipe(self):
        recept = recipe_model(
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
        assert bool(recept) == True

    def test_storage(self):
        storage = storage_model(name='Главный склад', adress='ул. Пушкина, д. Колотушкина, 23')

        assert storage is not None
        assert storage.name == 'Главный склад'
        assert len(storage.getattrs()) > 0 

    def test_storage_transaction(self):
        storage = storage_model(name='Главный склад', adress='ул. Пушкина, д. Колотушкина, 23')
        nomen = nomen_model(name='Яйца', group=nomen_group_model.create_group(), units=unit_model.create_count())
        counts = 300
        operations = True
        period = datetime.now()
        unit = unit_model.create_count()

        transaction = storage_transaction_model(storage=storage, nomen=nomen, operation=operations,
                                                countes=counts, unit=unit, period=period)

        assert transaction is not None

