from abc import ABC, abstractmethod


class convertor(ABC):

    @staticmethod
    @abstractmethod
    def convert(obj):
        pass