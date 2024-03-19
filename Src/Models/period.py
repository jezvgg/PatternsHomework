from Src.Models.abstract_references import abstract_referance
from datetime import datetime


class period(abstract_referance):
    __start: datetime
    __end: datetime

    def __init__(self, start: datetime, end: datetime, *args, **kwargs):
        self.__start: datetime = start
        self.__end: datetime = end
        super().__init__(*args, **kwargs)


    @property
    def start(self) -> datetime:
        return self.__start

    @property
    def end(self) -> datetime:
        return self.__end