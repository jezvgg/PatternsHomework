from Src.Models.abstract_references import abstract_referance
from Src.settings import Settings
from Utils.typecheck import typecheck


class organization_model(abstract_referance):
    __INN:str = ''
    __BIK:str = ''
    __account:str = ''
    __type:str = ''


    @typecheck
    def __init__(self, settings: Settings, *args, **kwargs):
        '''
        _INN, _BIK, _account, _type - you can get, but don't set.
        '''
        super().__init__(*args, **kwargs)
        for field in dir(self):
            if f'_{self.__class__.__name__}__' in field and hasattr(settings, field.replace(f'_{self.__class__.__name__}__', '')):
                setattr(self, field, getattr(settings, field.replace(f'_{self.__class__.__name__}__', '')))


    @property
    def INN(self):
        return self._INN


    @property
    def BIK(self):
        return self._BIK


    @property
    def account(self):
        return self._account


    @property
    def type(self):
        return self._type
