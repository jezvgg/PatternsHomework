from Src.settings import Settings
from Src.settings_manager import settings_manager
import unittest


class test_settings(unittest.TestCase):

    def test_check_first_name(self):
        sets = Settings()

        sets.first_name = "a  "

        assert sets.first_name == "a"


    def test_check_open_settings(self):
        item = settings_manager()

        result = item.open("settings.json")

        assert result == True


    def test_check_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()

        print(manager1.number)
        print(manager2.number)
        assert manager1.number == manager2.number


    def test_check_manager_convert(self):
        manager = settings_manager()

        manager.open('settings.json')

        sets = manager.convert()

        # Берём все неприватные поля и смотрим заполнены ли они
        assert all(getattr(sets, attr) for attr in filter(lambda x: not x.startswith('_'), dir(sets)))


    def test_check_manager_open(self):
        manager = settings_manager()
        assert manager.open("Tests/Settings.json")

