from Utils import typecheck
from Src.Storage.storage import storage
from Src.Logics.processes.process_storage_turn import process_storage_turn
from Src.exeptions import operation_exception


class process_factory:
    __maps: dict = {}


    def __init__(self):
        self.__build_structure()


    def __build_structure(self):
        self.__maps[storage.process_turn_key()] = process_storage_turn


    @typecheck
    def create(self, format: str, storage_: storage):
        if format not in self.__maps.keys():
            raise operation_exception("Нет подходящего обработчика")

        return self.__maps[format](journal=storage_.data[storage.journal_key()])
        