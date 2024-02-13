from pathlib import Path
from Src.settings import Settings
from Utils.typecheck import typecheck
from Src.exeptions import argument_exception, operation_exception
import json
import uuid
import os


class settings_manager(object):
    '''
    Класс для управления настройками.
    '''
    __file_name = 'settings.json'
    __unique_number = 0
    __data = {}
    __settings = None


    def __init__(self) -> None:
        self.__unique_number = uuid.uuid4()


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance


    def __convert(self):
        '''
        Конвертирует считаные данные из json в объект Settings
        '''
        if not len(self.__data):
            raise argument_exception("Невозможно создать объект типа Settings")

        fields = dir(self.__settings)

        for field in fields:
            if field not in self.data.keys(): continue
            setattr(self.__settings, field, self.data[field])


    def __open(self):
        settings_file = Path(Path.cwd(), self.__file_name)
        if not os.path.exists(settings_file):
            raise operation_exception("Невозможно открыть файл. Он не существует.")

        with open(settings_file) as read_file:
            self.__data = json.load(read_file)


    @typecheck(expression=lambda x: x['file_name'])
    def open(self, file_name: str) -> bool:
        '''
        Открывает файл настроек.

        Args:
            file_name: str - путь до файла ввиде строки
        '''
        self.__file_name = file_name.strip()

        try:
            self.__open()
        except Exception as exp:
            return False, exp
        

        return True
    

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