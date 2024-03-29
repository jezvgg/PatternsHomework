from Utils.typecheck import typecheck

class Settings:
    '''
    Класс хранения настроек.
    '''
    __firstname = ""
    __INN = 0
    __account = 0
    __corr_account = 0
    __BIK = 0
    __type = ""
    __first_start = True
    __rep_format = ''


    @property
    def first_name(self) -> str:
        return self.__firstname


    @first_name.setter
    @typecheck
    def first_name(self, value: str):
        '''
        Полное наименование
        '''
        self.__firstname = value.strip()


    @property
    def INN(self) -> int:
        return self.__INN


    @INN.setter
    @typecheck(expression=lambda x: len(str(x['value'])) == 12)
    def INN(self, value: int):
        '''
        ИНН
        '''
        self.__INN = value


    @property
    def account(self):
        return self.__account


    @account.setter
    @typecheck(expression=lambda x: len(str(x['value'])) == 11)
    def account(self, value: int):
        '''
        Счёт
        '''
        self.__account = value


    @property
    def correspondent_account(self):
        return self.__corr_account


    @correspondent_account.setter
    @typecheck(expression=lambda x: len(str(x['value'])) == 11)
    def correspondent_account(self, value: int):
        '''
        Корреспонденский счёт
        '''
        self.__corr_account = value


    @property
    def BIK(self):
        return self.__BIK


    @BIK.setter
    @typecheck(expression=lambda x: len(str(x['value'])) == 9)
    def BIK(self, value: int):
        '''
        БИК
        '''
        self.__BIK = value


    @property
    def type(self):
        return self.__type


    @type.setter
    @typecheck(expression=lambda x: len(x['value']) == 5)
    def type(self, value: str):
        '''
        Вид собственности
        '''
        if len(value) > 5: raise Exception("Некооректный вид собственности")

        self.__type = value.strip()


    @property
    def is_first_start(self):
        return self.__first_start


    @is_first_start.setter
    @typecheck
    def is_first_start(self, value: bool):
        self.__first_start = value


    @property
    def report_format(self):
        return self.__rep_format


    @report_format.setter
    @typecheck
    def report_format(self, value: str):
        self.__rep_format = value
