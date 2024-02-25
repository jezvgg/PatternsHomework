from Src.Models.abstract_references import abstract_referance
from Utils.typecheck import typecheck


class unit_model(abstract_referance):
    '''
    Единица измерения, надо чтоб были уникальные по названию.
    '''
    __base = None
    __num : int
    __coef: int


    @staticmethod
    def create_gramm():
        '''
        Создать единицу измерения грамм
        '''
        item = unit_model(name="грамм", base=None, coef=1)
        return item


    @staticmethod
    def create_kilogramm():
        '''
        Создать единицу измерения килограмм
        '''
        item = unit_model(name="килограмм", base=unit_model.create_gramm(), coef=1000)
        return item


    @staticmethod
    def create_count():
        '''
        Создать единицу измерения количества
        '''
        item = unit_model(name="штуки", base=None, coef=1)
        return item


    @staticmethod
    def create_milolitres():
        '''
            Создать единицу измерения жидкости
        '''
        return unit_model(name='миллилитры', base=None, coef=1)


    @staticmethod
    def create_litres():
        '''
            Создать единицу измерения жидкости
        '''
        return unit_model(name='литры', base=unit_model.create_milolitres(), coef=1000)


    def __init__(self, base = None, coef: int = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if base: self.__base = base
        self.__coef = coef


    @property
    def to_base(self):
        return unit_model(base=self.base.base, coef=self.base.coef, name=self.base.name)


    @property
    def base(self):
        return self.__base


    @property
    def coef(self):
        return self.__coef
