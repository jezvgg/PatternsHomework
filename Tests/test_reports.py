import unittest
from Src.Logics.report import report
from Src.Logics.report_csv import report_csv
from Src.settings_manager import settings_manager
from Src.Logics.start_factory import start_factory
from Src.Storage.storage import storage


class test_models(unittest.TestCase):

    def test_report(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        self.assertRaises(TypeError, report.__init__, factory.storage)

    def test_report_csv(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        csv = report_csv(factory.storage)

        result1 = csv.create(storage.unit_key())
        result2 = csv.create(storage.group_key())
        result3 = csv.create(storage.nomenculature_key())
        result4 = csv.create(storage.recipe_key())
        print(result1, result2, result3, result4)
        assert True == True