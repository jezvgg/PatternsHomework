import unittest
from Src.Logics.reports import *
from Src.settings_manager import settings_manager
from Src.Logics.start_factory import start_factory
from Src.Storage.storage import storage
from Src.Logics.reports.report_factory import report_factory
import json


class test_models(unittest.TestCase):

    def test_report(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        self.assertRaises(TypeError, report.__init__, factory.storage)

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

        print(csv.create(storage.unit_key()))

        with open('/home/jezvcp/Projects/PatternsHomework/Tests/smth.json', 'w', encoding='utf-8') as f:
            f.write(csv.create(storage.nomenculature_key()))

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
