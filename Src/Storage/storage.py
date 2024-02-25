


class storage:
    __data: dict = {}


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance


    @property
    def data(self) -> dict:
        return self.__data


    @property
    @staticmethod
    def nomenculature_key():
        return 'nomenculature'


    @property
    @staticmethod
    def group_key():
        '''
            Список номенкулатурных групп
        '''
        return 'group'

    @property
    @staticmethod
    def unit_key():
        '''
            Список единиц измерения
        '''
        return 'unit'

    
    @property
    @staticmethod
    def recipe_key():
        '''
            Список единиц измерения
        '''
        return 'unit'