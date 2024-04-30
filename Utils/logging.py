from functools import wraps
from Src.proxy import event_proxy


def logging(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        event_proxy(f'Успешно выпалнено {func.__name__}', func.__name__, 'DEBUG')
        return func(*args, **kwargs)

    return wrapper
        