


class storage:
    __data: dict = {}


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance


    @property
    def data(self) -> dict:
        return self.__data


    @staticmethod
    def nomenculature_key():
        return 'nomenculature'


    @staticmethod
    def log_key():
        return 'logging_key'


    @staticmethod
    def storages_key():
        return 'storages_key'


    @staticmethod
    def journal_key():
        return 'journal'


    @staticmethod
    def process_turn_key():
        return 'turns'


    @staticmethod
    def group_key():
        '''
            Список номенкулатурных групп
        '''
        return 'group'


    @staticmethod
    def turns_key() -> str:
        '''
            Предрасчитанные заранее обороты
        '''
        return 'turns'


    @staticmethod
    def unit_key() -> str:
        '''
            Список единиц измерения
        '''
        return 'unit'

    
    @staticmethod
    def recipe_key():
        '''
            Список единиц измерения
        '''
        return 'recipe'