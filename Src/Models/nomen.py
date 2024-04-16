from Src.Models import abstract_referance, nomen_group_model, unit_model
from Utils import attribute, typecheck


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


    @attribute(head='Полное имя')
    def full_name(self) -> str:
        return self.__full_name


    @attribute(head='Группа номенкулатуры')
    def group(self) -> nomen_group_model:
        return self.__group


    @attribute(head='Единицы измерения')
    def units(self) -> unit_model:
        return self.__units