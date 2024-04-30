from functools import wraps
from Src.proxy import event_proxy


def logging(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        event_proxy(f'Успешно выпалнено {func.__name__}', error_source=func.__name__, event_type_='DEBUG')
        return func(*args, **kwargs)

    return wrapper
        