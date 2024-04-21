from Src.settings import Settings
from Src.settings_manager import settings_manager
import unittest


class test_settings(unittest.TestCase):

    def test_settings(self):
        sets = Settings()

        sets.first_name = "a  "

        assert sets.first_name == "a"


    def test_open_manager(self):
        manager = settings_manager()

        manager.open("settings.json")
        manager.open("Tests/settings2.json")

        assert True == True


    def test_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()

        assert manager1.number == manager2.number


    def test_manager_convert(self):
        manager = settings_manager()

        manager.open('settings.json')
        sets = manager.settings

        # Берём все неприватные поля и смотрим заполнены ли они
        print(sets.get_attr_values('head'))
        assert all(sets.get_attr_values('head')) == True


    def test_menager_saving(self):
        manager = settings_manager()

        manager.open('settings.json')
        sets = manager.settings.get_attr_values('head')
        print('opened')

        manager.save()
        print('saved')
        manager.open('settings.json')
        sets2 = manager.settings.get_attr_values('head')
        
        assert all([setting1==setting2 for setting1, setting2 in zip(sets, sets2)]) == True
