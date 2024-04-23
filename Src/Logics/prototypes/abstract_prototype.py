from Utils import typecheck
from abc import abstractclassmethod, ABC


class abstract_prototype(ABC):
    _data: list = []


    @typecheck
    def __init__(self, data: list):
        self._data = data


    @abstractclassmethod
    def filter_by(self, filter_model):
        pass


    @property
    def data(self) -> list:
        return self._data