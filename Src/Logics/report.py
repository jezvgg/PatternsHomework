from abc import ABC, abstractmethod
from Src.Storage.storage import storage


class report(ABC):
    _storage: storage
    

    def __init__(self, storage_: storage):
        self._storage = storage_


    @abstractmethod
    def create(self) -> str:
        pass