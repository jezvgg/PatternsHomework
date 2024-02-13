from Src.settings_manager import settings_manager
from Models import *
import unittest


class test_models(unittest.TestCase):

    def test_unit(self):
        units = unit(name='gram', num=790)

        assert units.num == 790
        assert units.name == 'gram'
        assert str(units) == "790 gram"

    def test_big_unit(self):
        gram = unit(name='gram', num=990)
        kilogram = unit(base=gram, num=2, coef=1000, name='kilogram')

        gram_in_kilo = kilogram.to_base

        assert gram_in_kilo.name == 'gram'
        assert gram_in_kilo.base == None
        assert gram_in_kilo.num == 2000

    def test_biggest_unit(self):
        bit = unit(name='bit')
        bite = unit(name='bite', base=bit, coef=8)
        kilobite = unit(name='kilobite', base=bite, coef=1024, num=3)

        assert kilobite.to_base.to_base.name == 'bit'
        assert kilobite.to_base.to_base.num == 24576

    def test_organizations(self):
        manager = settings_manager()
        manager.open('settings.json')
        org = organization(settings=manager.settings, name='org')
        
