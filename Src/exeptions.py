from Src.proxy import event_proxy


class exceptions(Exception):


    def __init__(self, text: str = '',*args, **kwargs):
        super().__init__(text, *args, **kwargs)
        # event_proxy(text, error_source='', event_type_='ERROR')


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
