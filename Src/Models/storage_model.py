from Src.Models import abstract_referance
from Utils import typecheck, attribute


class storage_model(abstract_referance):
    __adress: str = ''


    @typecheck
    def __init__(self, adress: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__adress = adress


    @attribute(head='Адрес')
    def adress(self) -> str:
        return self.__adress
    