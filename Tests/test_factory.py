import unittest
from Models import *
from Logics.start_factory import start_factory
from Src.settings_manager import settings_manager


class test_factory(unittest.TestCase):

    def test_create_factory(self):
        unit = unit_model.create_kilogramm()

        assert unit is not None

    def test_start_factory(self):
        nomens = start_factory.create_nomenculature()

        assert nomens is not None
        assert len(nomens) != 0

    def test_factory_create(self):
        manager = settings_manager()
        nomens = start_factory(manager.settings).create()

        assert len(nomens) > 0
