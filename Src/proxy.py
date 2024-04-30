from Utils.AttrWorker import AttrWorker
from Utils.attribute import attribute
from Src.Logics.observer import observer
from Src.Logics.event_type import event_type
from datetime import datetime


class event_proxy(AttrWorker):
    __message = ''
    __event_type = ''
    __source = ''
    __datetime: datetime


    def __init__(self, message: str = '', source: str = '', event_type_ = 'DEBUG', datetime = datetime.now()):
        self.source = source
        self.__message = message
        self.__event_type = event_type_
        self.__datetime = datetime
        observer.raise_event(event_type.add_log(), self)


    def __repr__(self):
        return f'event_proxy({self.message}, {self.source}, {self.__event_type}, {self.datetime})'


    @attribute(head='Сообщение')
    def message(self) -> str:
        '''
            Сообщение события
        '''
        return self.__message


    @message.setter
    def message(self, value: str):
        if not isinstance(value, str):
            raise TypeError("error_message must be string!")

        if not value.strip():
            self.__is_error = False
            return

        self.__message = value.strip()


    @attribute(head='Тип лога')
    def event_type_(self) -> str:
        return self.__event_type


    @attribute(head='Период')
    def datetime(self) -> datetime:
        return self.__datetime


    @attribute(head='Источник')
    def source(self) -> str:
        '''
            Источник лога.
        '''
        return self.__source


    @source.setter
    def source(self, value: str):
        if not isinstance(value, str):
            raise TypeError("error_source must be string!")
        if not value: return

        self.__source = value
        