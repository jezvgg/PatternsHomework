from settings import Settings
from settings_manager import settings_manager
import unittest


class test_settings(unittest.TestCase):

    def test_check_first_name(self):
        sets = Settings()

        sets.first_name = "a  "

        assert sets.first_name == "a"

    def test_check_open_settings(self):
        item = settings_manager()

        result = item.open("settings.json")

        print(item.data)
        assert result == True

    def test_check_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()

        print(manager1.number)
        print(manager2.number)
        assert manager1.number == manager2.number

    def test_check_manager_convert(self):
        manager = settings_manager()
        manager.open("settings.json")

        manager.convert()


