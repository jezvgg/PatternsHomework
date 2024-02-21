from Models import abstract_referance, nomen_group_model, unit_model
from Utils.typecheck import typecheck


class nomen_model(abstract_referance):
    __full_name = ''
    __group = None
    __units = None


    @typecheck(expression = lambda x: len(x['full_name']) < 256)
    def __init__(self, name: str, group: nomen_group_model, units: unit_model, full_name: str = '', *args, **kwargs):
        super().__init__(name, *args, **kwargs)

        self.__full_name = full_name
        if not full_name and name:
            self.__full_name = name
        self.__units = units
        self.__group = group


    @property
    def full_name(self):
        return self.__full_name


    @property
    def group(self):
        return self.__group


    @property
    def units(self):
        return self.__units