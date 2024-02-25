import unittest
from Src.Models import *
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage


class test_factory(unittest.TestCase):

    def test_create_factory(self):
        unit = unit_model.create_kilogramm()

        assert unit is not None

    def test_start_factory(self):
        nomens = start_factory.create_nomenculature()
        recepts = start_factory.create_recipets()

        assert nomens is not None
        assert len(nomens) != 0
        assert recepts is not None
        assert len(recepts) != 0

    def test_factory_create(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)
        
        result = factory.create()

        assert len(result) > 0
        assert factory.storage is not None
        assert storage.nomenculature_key in factory.storage.data
        assert storage.group_key in factory.storage.data
        assert storage.unit_key in factory.storage.data
