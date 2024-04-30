import unittest
from Src.settings_manager import settings_manager
from Src.Logics.start_factory import start_factory
from Src.Storage.storage import storage
from Src.Logics.reports.converter import deconvertor
from Src.proxy import event_proxy

class test_proxy(unittest.TestCase):

    def test(self):
        manager = settings_manager()
        start = start_factory(manager.settings)

        event = event_proxy("test", "Test")
        
        print(start.storage.data[storage.log_key()])
        assert start.storage.data[storage.log_key()][-1] == event
        
        