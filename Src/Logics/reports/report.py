from abc import ABC, abstractmethod
from Src.Storage.storage import storage
from Src.settings import Settings
from Utils import typecheck


class report(ABC):
    _storage: storage
    _settings: Settings
    

    @typecheck
    def __init__(self, storage_: storage):
        self._storage = storage_


    @abstractmethod
    def create(self) -> str:
        pass