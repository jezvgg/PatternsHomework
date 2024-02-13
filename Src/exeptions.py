from Src.error_proxy import error_proxy


class exceptions(Exception):
    __inner_error: error_proxy = error_proxy()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__inner_error.set_error(self)


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
