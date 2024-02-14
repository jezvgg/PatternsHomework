from Models.abstract_references import abstract_referance
from Src.settings import Settings
from Utils.typecheck import typecheck


class organization(abstract_referance):
    _INN:str = ''
    _BIK:str = ''
    _account:str = ''
    _type:str = ''


    @typecheck
    def __init__(self, settings: Settings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in dir(self):
            if hasattr(settings, field[1:]):
                setattr(self, field, getattr(settings, field[1:]))

