

class event_type(object):
    __name: str
    change_block_period = None
    delete_nomenculature = None
    add_log = None
    create_log = None



    def __init__(self, name: str):
        self.__name = name


    def __new__(cls, name: str):
        if not hasattr(cls, name):
            setattr( cls, name, super(event_type, cls).__new__(cls))
        return getattr(cls, name)
    
    
    @staticmethod
    def change_block_period():
        return event_type('change_block_period')
    
    @staticmethod
    def delete_nomenculature():
        return event_type('delete_nomenculature')

    @staticmethod
    def add_log():
        return event_type('add_log')

    @staticmethod
    def create_log():
        return event_type('create_log')