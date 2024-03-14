from Utils import typecheck
from abc import ABC, abstractmethod
from Src.Models import storage_transaction_model


class abstract_process(ABC):
    operations = {True: 1, False: -1}

    @abstractmethod
    def create(self):
        pass