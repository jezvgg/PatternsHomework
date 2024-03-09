from functools import wraps
from Src.exeptions import argument_exception
from Utils.instance import instance_checker


def typecheck(_func = None, expression = lambda x: True):

    def typechecker(func):
        '''
        Декоратор для проверки входных функций.

        На вход может принимать функцию условие на аргументы.
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            arguments = list(args)[:]
            if func.__defaults__:
                arguments = list(args)+list(func.__defaults__)

            var = {}
            for varname in func.__code__.co_varnames:
                if varname in kwargs.keys(): 
                    var[varname] = kwargs[varname]
                    continue
                if arguments:
                    var[varname] = arguments.pop(0)

            anot = func.__annotations__

            # print(var, anot)

            for key in anot.keys():
                if (anot and key not in anot.keys()) or key == 'return': continue
                if not instance_checker(var[key], anot[key]):
                    raise argument_exception("Несоответсвие типов.")
                
            if expression and not expression(var):
                raise argument_exception("Передаваемые аргументы не соответсвтуют ограничениям.")

            result = func(*args, **kwargs)

            if 'return' in anot.keys() and not instance_checker(result, anot['return']):
                raise argument_exception("Несоответсвие типов.")

            return result
        
        return wrapper
    
    if _func is None:
        return typechecker
    return typechecker(_func)