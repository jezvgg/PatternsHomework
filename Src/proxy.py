from Utils import AttrWorker, attribute
from Src.Logics.observer import observer
from Src.Models import event_type
from datetime import datetime


class event_proxy(AttrWorker):
    __message = ''
    __event_type = ''
    __error_source = ''
    __is_error = ''
    __datetime: datetime


    def __init__(self, error_message: str = '', error_source: str = '', event_type_ = '', datetime = datetime.now()):
        self.error_source = error_source
        self.__message = error_message
        self.__event_type = event_type_
        self.__datetime = datetime
        observer.raise_event(event_type.add_log(), self)


    @attribute(head='Сообщение')
    def message(self):
        '''
            Текст ошибки
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
        self.__is_error = True


    @attribute(head='Тип лога')
    def event_type(self):
        return self.__event_type


    @attribute(head='Период')
    def datetime(self):
        return self.__datetime

    @property
    def error_source(self):
        '''
            Источник ошибки.
        '''
        return self.__error_source


    @error_source.setter
    def error_source(self, value: str):
        if not isinstance(value, str):
            raise TypeError("error_source must be string!")
        if not value: return

        self.__error_source = value
        

    @property
    def is_error(self):
        '''
            Флаг. Есть ошибка.
        '''
        return self.__is_error


    def set_error(self, exception: Exception):
        '''
            Сохранить ошибку.
        '''
        if not isinstance(exception, Exception):
            self.error_message = "Некорректно переданы параметры."
            self.error_source = 'set_error()'
            return

        if exception:
            self.error_message = f'ОШИБКА! {str(exception)}'
            self.error_source = f'ИСКЛЮЧЕНИЕ! {type(exception)}'
            return

        self.__message = ''
        