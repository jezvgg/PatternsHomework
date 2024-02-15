from functools import wraps
from Src.exeptions import argument_exception


def typecheck(_func = None, expression = lambda x: True):

    def typechecker(func):
        '''
        Декоратор для проверки входных функций.

        На вход может принимать функцию условие на аргументы.
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            var = dict(zip(func.__code__.co_varnames, args)) | kwargs
            anot = func.__annotations__
            for key in var.keys():
                if key not in anot.keys(): continue
                if not isinstance(var[key], anot[key]):
                    raise argument_exception("Несоответсвие типов.")
                
            if expression and not expression(var):
                raise argument_exception("Передаваемые аргументы не соответсвтуют ограничениям.")
        
            return func(*args, **kwargs)
        
        return wrapper
    
    if _func is None:
        return typechecker
    return typechecker(_func)