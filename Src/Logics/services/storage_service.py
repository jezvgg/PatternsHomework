from Src.Logics.prototypes.storage_prototype import storage_prototype
from Src.exeptions import operation_exception, argument_exception
from Src.Logics.processes import process_factory
from Src.Logics.services import abstract_service
from functools import singledispatchmethod
from Src.Storage.storage import storage
from Src.Models import period
from datetime import datetime
from Utils import logging
from Src.Logics.event_type import event_type
from Src.Models import *


class storage_service(abstract_service):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._events[event_type.change_block_period()] = self.create_blocked_turns


    @singledispatchmethod
    def create_turns(self, obj, **kwargs):
        raise operation_exception(f"Нет сервиса для {type(obj)}.")


    @create_turns.register
    @logging
    def create_turns_by_period(self, obj: period, **kwargs):
        prototype = storage_prototype( self.data )
        transactions = prototype.filter_by( obj ).data
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)
        return rests


    @create_turns.register
    @logging
    def create_turns_by_nomen(self, obj: nomen_model, **kwargs):
        storage_ = None
        prototype = storage_prototype( self.data )
        transactions = prototype.filter_by( obj )
        if 'storage' in kwargs.keys() and kwargs['storage']: 
            transactions = transactions.filter_by( kwargs['storage'] )
        processing = process_factory().create(storage.process_turn_key())
        return processing.create(transactions.data)


    @create_turns.register
    @logging
    def create_turns_by_recipe(self, obj: recipe_model, **kwargs):
        if 'storage' not in kwargs.keys(): raise argument_exception("Для создания оборотов по рецепту, нужно передать склад!")
        prototype = storage_prototype( self.data )
        transactions = prototype.filter_by( kwargs['storage'] ).filter_by( obj ).data
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)
        return rests


    @logging
    def create_blocked_turns(self):
        
        turn_period = period(datetime.strptime('1900-01-01', '%Y-%m-%d'), self._manager.settings.block_period)
        
        self._storage.data[storage.turns_key()] = self.create_turns(turn_period)

        return True


    @logging
    def create_debits(self, obj: recipe_model, storage_: storage_model):
        turns = self.create_turns(obj, storage=storage_)

        recipe_need = {}
        for recipe_row in obj.rows:
            recipe_need[recipe_row.nomenculature.name] = recipe_row.size

        transactions = []
        for turn in turns:
            if recipe_need[turn.nomen.name] > turn.remains:
                raise operation_exception('Не удалось произвести списование! Остатков на складе не достаточно!')
            transactions.append(storage_transaction_model(storage=storage_, nomen=turn.nomen, operation=False, 
                                                        countes=recipe_need[turn.nomen.name], unit=turn.unit, period=datetime.now()))

        return transactions