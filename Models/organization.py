from Models.abstract_references import abstract_referance
from Src.settings import Settings
from Utils.typecheck import typecheck


class organization(abstract_referance):
    __INN:str
    __BIK:str
    __account:str
    __type:str


    def __init__(self, settings: Settings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(dir(settings))

