from functools import wraps

class result_int(int): pass
class result_float(float): pass
class result_list(list): pass
class result_tuple(tuple): pass
class result_string(str): pass
class result_dict(dict): pass


results = {int:result_int, float:result_float, list:result_list, tuple:result_tuple,str:result_string,dict:result_dict,type(None):result_string,bool:result_string}


def header(_func = None, name =''):

    def export_header(func):
        name_ = name
        if not name_: name_ = func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            var = func(*args, **kwargs)
            result = var
            if type(var) in results.keys():
                result = results[type(var)](var)
            setattr(result, 'head', name_)

            return result
        return wrapper

    if _func is None:
        return export_header
    return export_header(_func)
