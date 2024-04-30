import unittest
from Src.Logics.reports import *
from Src.settings_manager import settings_manager
from Src.Logics.start_factory import start_factory
from Src.Storage.storage import storage
from Src.exeptions import argument_exception
from Src.settings import Settings
from Src.Models import *
import datetime


class test_reports(unittest.TestCase):

    def test_report(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        assert 1 == 1

    def test_report_csv(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        csv = report_csv(factory.storage)

        assert csv.create(storage.unit_key()) != ''
        assert csv.create(storage.nomenculature_key()) != ''

    def test_report_markdown(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        csv = report_markdown(factory.storage)

        assert csv.create(storage.unit_key()) != ''
        assert csv.create(storage.nomenculature_key()) != ''

    def test_report_json(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        csv = report_json(factory.storage)

        print(csv.create(storage.recipe_key()))

        with open('smth.json', 'w') as f:
            f.write(csv.create(storage.recipe_key()))

        assert csv.create(storage.unit_key()) != ''
        assert csv.create(storage.nomenculature_key()) != ''

    def test_report_factory(self):
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = report_factory()

        result = factory.create(manager.settings.report_format, start.storage)

        assert bool(result) == True
        print(result.create(storage.unit_key()))
        assert len(result.create(storage.unit_key())) > 0

    def test_convertor_basic(self):
        assert convertor_basic.convert(5) == 5
        assert convertor_basic.convert('g') == 'g'
        self.assertRaises(argument_exception,convertor_basic.convert,datetime.datetime.now())

    def test_convertor_datetime(self):
        data = convertor_datetime.convert(datetime.datetime.now())

        assert data is not None
        assert 'Год' in data.keys() and 'Секунды' in data.keys()

    def test_convertor_model(self):
        data = convertor_models.convert(unit_model.create_gramm())

        assert data is not None
        
        kilodata = convertor_models.convert(unit_model.create_kilogramm())

        assert kilodata is not None

    def test_deconvertor_model(self):
        result = deconvertor().load('Tests/nomen.json', dtype=nomen_model)
        assert isinstance(result, nomen_model) == True
        print('nomen done')
        result = deconvertor().load('Tests/list_nomens.json', dtype=list[nomen_model])
        assert isinstance(result, list) == True
        print('list nomens done')
        result = deconvertor().load('Tests/recipe.json', dtype=recipe_model)
        assert isinstance(result, recipe_model) == True
        print('recipe done')
        result = deconvertor().load('Tests/settings2.json', dtype=Settings)
        assert isinstance(result, Settings) == True
        print('recipe done')

