from pathlib import Path
from Src.settings import Settings
from Utils.typecheck import typecheck
from Src.exeptions import argument_exception, operation_exception
from Src.Logics.reports.converter import deconvertor, convert_factory
from Src.Logics.reports.report_json import report_json
import json
import uuid
import os


class settings_manager(object):
    '''
    Класс для управления настройками.
    '''
    __unique_number = 0
    __data = {}
    __settings = None


    def __init__(self) -> None:
        self.__unique_number = uuid.uuid4()
        self.open('settings.json')


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance


    def open(self, file_name: str = 'settings.json'):
        self.__settings = deconvertor().load(file_name, Settings)


    def save(self, file_name: str = 'settings.json') -> str:
        with open(file_name, 'w') as f:
            result = json.dumps({str(key):convert_factory.create(value).convert(value) for key, value in self.__settings.get_by_attr('head').items()}, ensure_ascii=False, indent=4)
            f.write(result)
        return result


    @property
    def data(self) -> dict:
        '''
        Вернёт словарь значений json.
        '''
        return self.__data


    @property
    def number(self) -> int:
        '''
        Уникальный номер синглтона
        '''
        return self.__unique_number
    

    @property
    def settings(self) -> Settings:
        '''
        Возращает открытые настройки
        '''
        if not self.__settings:
            self.__convert()
        return self.__settings