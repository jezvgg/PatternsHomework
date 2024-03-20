from Src.Logics.storage_service import storage_service
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from datetime import datetime
from Src.Models import *
import unittest



class test_models(unittest.TestCase):

    def test_period_turns(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()

        start_date = datetime.strptime('2023-01-01', '%Y-%m-%d')
        stop_date = datetime.strptime('2024-10-01', '%Y-%m-%d')

        service = storage_service(start.storage.data[storage.journal_key()])
        result = service.create_turns(period(start=start_date, end=stop_date))

        assert result is not None
        assert len(result) != 0


    def test_nomen_turns(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()

        nomen = nomen_model(name='Сахар', group=nomen_group_model.create_group(), units=unit_model.create_gramm())

        service = storage_service(start.storage.data[storage.journal_key()])
        result = service.create_turns( nomen )

        assert result is not None
        assert len(result) != 0


    def test_recipe_debits(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()

        recipe = start.storage.data[storage.recipe_key()][0]
        storage_ = start.storage.data[storage.storages_key()][0]

        service = storage_service(start.storage.data[storage.journal_key()])
        result = service.create_turns( recipe , storage=storage_)

        assert result is not None
        assert len(result) != 0

