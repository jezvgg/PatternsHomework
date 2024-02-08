
class Settings:
    __firstname = ""


    @property
    def first_name(self):
        return self.__firstname


    @first_name.setter
    def first_name(self, value: str):
        '''
        Полное наименование
        '''
        if not isinstance(value, str):
            raise TypeError("Некорректный аргумент.")

        self.__firstname = value.strip()
