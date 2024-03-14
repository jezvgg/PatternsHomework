from Utils import typecheck
from abc import ABC, abstractmethod
from Src.Models import storage_transaction_model


class abstract_process(ABC):
    _journal = []
    operations = {True: 1, False: -1}


    @typecheck
    def __init__(self, journal: list[storage_transaction_model]):
        self._journal = journal


    @abstractmethod
    def create(self):
        pass