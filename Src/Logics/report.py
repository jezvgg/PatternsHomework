from abc import ABC, abstractmethod
from Src.Storage.storage import storage
from Src.settings import Settings


class report(ABC):
    _storage: storage
    _settings: Settings
    

    def __init__(self, storage_: storage, settings: Settings):
        self._storage = storage_
        self._settings = settings


    @abstractmethod
    def create(self) -> str:
        pass