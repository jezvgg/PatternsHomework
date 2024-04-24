from Src.Logics.services import storage_service, nomenculature_service
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from datetime import datetime
from Src.Models import *
import unittest
import json



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


    def test_recipe_turns(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()

        recipe = start.storage.data[storage.recipe_key()][0]
        storage_ = start.storage.data[storage.storages_key()][0]

        service = storage_service(start.storage.data[storage.journal_key()])
        result = service.create_turns( recipe , storage=storage_)

        assert result is not None
        assert len(result) != 0


    def test_recipe_devits(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()

        recipe = start.storage.data[storage.recipe_key()][0]
        storage_ = start.storage.data[storage.storages_key()][0]

        service = storage_service(start.storage.data[storage.journal_key()])
        result = service.create_debits( recipe , storage_)

        assert result is not None
        assert len(result) != 0


    def test_get_nomenculature(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()

        service = nomenculature_service(start.storage.data[storage.nomenculature_key()])
        nomen = start.storage.data[storage.nomenculature_key()][0]
        result = service.get_nomenculature(nomen.id)

        assert result == nomen

    
    def test_del_nomenculature(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()

        print(start.storage.data[storage.nomenculature_key()])

        service = nomenculature_service(start.storage.data[storage.nomenculature_key()])
        nomen = start.storage.data[storage.nomenculature_key()][0]
        result = service.del_nomenculature(nomen.id)

        print('\n\n\n',start.storage.data[storage.nomenculature_key()])

        assert result == True
        assert service.get_nomenculature(nomen.id) is False
        assert start.storage.data[storage.nomenculature_key()][0] != nomen


    def test_add_nomenculature(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()
        service = nomenculature_service(start.storage.data[storage.nomenculature_key()])

        with open('Tests/nomen.json') as f:
            nomen_json = json.load(f)

        nomen_id = nomen_json['Код']
        result = service.add_nomenculature(nomen_json)

        assert result == True
        assert service.get_nomenculature(nomen_id) is not None

    
    def test_patch_nomenculature(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()
        service = nomenculature_service(start.storage.data[storage.nomenculature_key()])

        with open('Tests/nomen.json') as f:
            nomen_json = json.load(f)

        nomen_id = nomen_json['Код']
        old_nomen_id = start.storage.data[storage.nomenculature_key()][0].id
        result = service.change_nomenculature(old_nomen_id, nomen_json)

        assert result == True
        print(service.get_nomenculature(old_nomen_id))
        assert service.get_nomenculature(old_nomen_id) is False
        assert service.get_nomenculature(nomen_id) is not None


    def test_blocked_turns(self):
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()

        service = storage_service(start.storage.data[storage.journal_key()])
        result = service.create_blocked_turns()

        assert result == True 

