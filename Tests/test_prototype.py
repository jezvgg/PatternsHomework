from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from datetime import datetime
import unittest


class test_prototype(unittest.TestCase):

    def test_prototype(self):
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()

        key = storage.journal_key()
        data = start.storage.data[key]

        prototype = storage_prototype( data )

        start_date = datetime.strptime("2024-01-01", '%Y-%m-%d')
        stop_date = datetime.strptime("2024-01-10", '%Y-%m-%d')

        result = prototype.filter( start_date, stop_date )

        assert isinstance(result, storage_prototype)