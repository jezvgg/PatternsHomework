import unittest
from Src.Storage.storage import storage
from Src.Logics.processes.process_factory import process_factory
from Src.settings_manager import settings_manager
from Src.Logics.start_factory import start_factory


class test_processes(unittest.TestCase):
    
    def test_process_factory(self):
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()

        process = process_factory().create(format=storage.process_turn_key(), storage_=start.storage)
        result = process.create(start.storage.data[storage.journal_key()])

        for turn in result:
            print(f"Со склада {turn.storage.name} оборот {turn.nomen.name} равняется {turn.remains} {turn.unit.name}")

        assert result is not None