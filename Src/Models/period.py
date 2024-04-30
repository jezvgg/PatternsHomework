from datetime import datetime


class period:
    __start: datetime
    __end: datetime

    def __init__(self, start: datetime, end: datetime):
        self.__start: datetime = start
        self.__end: datetime = end


    @property
    def start(self) -> datetime:
        return self.__start

    @property
    def end(self) -> datetime:
        return self.__end