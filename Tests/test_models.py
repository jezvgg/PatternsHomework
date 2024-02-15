from Src.settings_manager import settings_manager
from Src.exeptions import argument_exception
from Models import *
import unittest


class test_models(unittest.TestCase):

    def test_abs(self):
        abc = abstract_referance(name='name')

        assert abc.name == 'name'
        self.assertRaises(argument_exception, abstract_referance, name='1234567890'*10)

    def test_unit(self):
        units = unit_model(name='gram', num=790)

        assert units.num == 790
        assert str(units) == "790 gram"

    def test_big_unit(self):
        gram = unit_model(name='gram', num=990)
        kilogram = unit_model(base=gram, num=2, coef=1000, name='kilogram')

        gram_in_kilo = kilogram.to_base

        assert gram_in_kilo.name == 'gram'
        assert gram_in_kilo.base == None
        assert gram_in_kilo.num == 2000

    def test_biggest_unit(self):
        bit = unit_model(name='bit')
        bite = unit_model(name='bite', base=bit, coef=8)
        kilobite = unit_model(name='kilobite', base=bite, coef=1024, num=3)

        assert kilobite.to_base.to_base.name == 'bit'
        assert kilobite.to_base.to_base.num == 24576

    def test_organizations(self):
        manager = settings_manager()
        manager.open('settings.json')
        organ = organization_model(settings=manager.settings, name='org')

        assert all(filter(lambda x: x.startswith('_'), dir(organ)))

    def test_nomen_group(self):
        group = nomen_group_model(name='Group one')

        assert bool(group) == True

    def test_nomen(self):
        nom = nomen_model(name="nomen1", full_name='big_nomen_2', group = nomen_group_model('Group'), units=unit_model(name='unit'))

        assert bool(nom) == True
