import unittest
from datetime import datetime
from Src.settings_manager import settings_manager
from Src.Logics.start_factory import start_factory
from Src.Storage.storage import storage


class test_events(unittest.TestCase):

    def test_change_block_period(self):
        manager = settings_manager()
        start = start_factory(manager.settings)

        before = start.storage.data[storage.turns_key()]
        manager.settings.block_period = datetime.strptime('2025-10-4', '%Y-%m-%d')
        after = start.storage.data[storage.turns_key()]

        print(before)
        print(after)

        assert before != after