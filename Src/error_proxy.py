from Utils.typecheck import typecheck


class error_proxy:

    __error_message = ''
    __error_source = ''
    __is_error = ''


    def __init__(self, error_message: str = '', error_source: str = ''):
        self.error_source = error_source
        self.error_message = error_message



    @property
    def error_message(self):
        '''
            Текст ошибки
        '''
        return self.__error_message


    @error_message.setter
    @typecheck
    def error_message(self, value: str):
        if not value.strip():
            self.__is_error = False
            return

        self.__error_message = value.strip()
        self.__is_error = True


    @property
    def error_source(self):
        '''
            Источник ошибки.
        '''
        return self.__error_source


    @error_source.setter
    @typecheck
    def error_source(self, value: str):
        if not value: return
        self.__error_source = value
        

    @property
    def is_error(self):
        '''
            Флаг. Есть ошибка.
        '''
        return self.__is_error


    def set_error(self, exception: Exception):
        '''
            Сохранить ошибку.
        '''
        if not isinstance(exception, Exception):
            self.error_message = "Некорректно переданы параметры."
            self.error_source = 'set_error()'
            return

        if exception:
            self.error_message = f'ОШИБКА! {str(exception)}'
            self.error_source = f'ИСКЛЮЧЕНИЕ! {type(exception)}'
            return

        self.error_message = ''
        