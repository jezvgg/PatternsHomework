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

        assert manager.open("settings.json")
        assert manager.open("Tests/settings2.json")


    def test_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()

        assert manager1.number == manager2.number


    def test_manager_convert(self):
        manager = settings_manager()

        manager.open('settings.json')
        sets = manager.convert()

        # Берём все неприватные поля и смотрим заполнены ли они
        assert all(getattr(sets, attr) for attr in filter(lambda x: not x.startswith('_'), dir(sets)))
