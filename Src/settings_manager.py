from pathlib import Path
from Src.settings import Settings
from Utils.typecheck import typecheck
import json
import uuid
import os


class settings_manager(object):
    __file_name = 'settings.json'
    __unique_number = 0
    __data = {}
    __settings = Settings()


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance


    def convert(self):
        if not len(self.__data):
            raise Exception("Невозможно создать объект типа Settings")

        fields = dir(self.__settings)

        for field in fields:
            if field not in self.data.keys(): continue
            setattr(self.__settings, field, self.data[field])
        
        return self.__settings


    def __init__(self) -> None:
        self.__unique_number = uuid.uuid4()


    @property
    def data(self) -> dict:
        '''
        Вернёт словарь значений json.
        '''
        return self.__data


    @property
    def number(self):
        return self.__unique_number


    def __open(self):
        settings_file = Path(Path.cwd(), self.__file_name)
        if not os.path.exists(settings_file):
            raise Exception("Невозможно открыть файл. Он не существует.")

        with open(settings_file) as read_file:
            self.__data = json.load(read_file)


    @typecheck(expression=lambda x: x['file_name'])
    def open(self, file_name: str) -> bool:
        self.__file_name = file_name.strip()

        try:
            self.__open()
        except Exception as exp:
            return False, exp
        

        return True