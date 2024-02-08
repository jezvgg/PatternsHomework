from Utils.typecheck import typecheck

class Settings:
    __firstname = ""
    __INN = 0
    __account = 0
    __corr_account = 0
    __BIK = 0
    __type = ""


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
