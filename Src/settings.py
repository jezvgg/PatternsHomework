from Utils import typecheck, attribute, AttrWorker
from Src.Logics.observer import observer
from Src.Logics.event_type import event_type
from datetime import datetime


class Settings(AttrWorker):
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
    __block_period = None


    def __init__(self, first_name: str = '', INN: str = '', account: int = 0, 
                correspondent_account: int = 0, BIK: str = '', type: str = '',
                is_first_start: bool = False, report_format: str = '', block_period: datetime = datetime.now()):
        self.__firstname = first_name
        self.__INN = INN
        self.__account = account
        self.__corr_account = correspondent_account
        self.__BIK = BIK
        self.__first_start = is_first_start
        self.__rep_format = report_format
        self.__block_period = block_period
        self.__type = type


    @attribute(head='Наименование')
    def first_name(self) -> str:
        return self.__firstname


    @first_name.setter
    @typecheck
    def first_name(self, value: str):
        '''
        Полное наименование
        '''
        self.__firstname = value.strip()


    @attribute(head='ИНН')
    def INN(self) -> int:
        return self.__INN


    @INN.setter
    @typecheck(expression=lambda x: len(str(x['value'])) == 12)
    def INN(self, value: int):
        '''
        ИНН
        '''
        self.__INN = value


    @attribute(head='Счёт')
    def account(self) -> int:
        return self.__account


    @account.setter
    @typecheck(expression=lambda x: len(str(x['value'])) == 11)
    def account(self, value: int):
        '''
        Счёт
        '''
        self.__account = value


    @attribute(head='Корреспонденский счёт')
    def correspondent_account(self) -> int:
        return self.__corr_account


    @correspondent_account.setter
    @typecheck(expression=lambda x: len(str(x['value'])) == 11)
    def correspondent_account(self, value: int):
        '''
        Корреспонденский счёт
        '''
        self.__corr_account = value


    @attribute(head='БИК')
    def BIK(self) -> str:
        return self.__BIK


    @BIK.setter
    @typecheck(expression=lambda x: len(str(x['value'])) == 9)
    def BIK(self, value: int):
        '''
        БИК
        '''
        self.__BIK = value


    @attribute(head='Вид собственности')
    def type(self) -> str:
        return self.__type


    @type.setter
    @typecheck(expression=lambda x: len(x['value']) == 5)
    def type(self, value: str):
        '''
        Вид собственности
        '''
        if len(value) > 5: raise Exception("Некооректный вид собственности")

        self.__type = value.strip()


    @attribute(head='Первый запуск')
    def is_first_start(self) -> bool:
        return self.__first_start


    @is_first_start.setter
    @typecheck
    def is_first_start(self, value: bool):
        self.__first_start = value


    @attribute(head='Тип выгрузки')
    def report_format(self) -> str:
        return self.__rep_format


    @report_format.setter
    @typecheck
    def report_format(self, value: str):
        self.__rep_format = value


    @attribute(head='Дата блокировки')
    def block_period(self) -> datetime:
        return self.__block_period


    @block_period.setter
    @typecheck
    def block_period(self, value: datetime):
        self.__block_period = value
        observer.raise_event(event_type.change_block_period())
