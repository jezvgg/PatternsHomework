from Utils import typecheck
from datetime import datetime
from Src.Models import storage_transaction_model


class storage_prototype:
    __data: list[storage_transaction_model] = []


    @typecheck
    def __init__(self, data: list[storage_transaction_model]):
        self.__data = data


    @typecheck(expression=lambda x: x['start_period'] <= x['stop_period'])
    def filter(self, start_period: datetime, stop_period: datetime):
        result = []
        for item in self.data:
            if item.period > start_period and item.period <= stop_period:
                result.append(item)

        return storage_prototype(result)


    @property
    def data(self) -> list:
        return self.__data

