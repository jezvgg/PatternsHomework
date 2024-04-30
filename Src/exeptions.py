


class exceptions(Exception):
    __inner_error: None


    def __init__(self, text: str = '',*args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.__inner_error.set_error(self)
        # event_proxy(text, error_source='', event_type_='ERROR')
        


    @property
    def error(self):
        return self.__inner_error


class argument_exception(exceptions):
    '''
    Ошибка передачи аргументов. Несоответсвие типов. Несоответсвие условиям.
    '''
    pass


class operation_exception(exceptions):
    '''
    Ошибка выполнения определённой операции.
    '''
    pass
