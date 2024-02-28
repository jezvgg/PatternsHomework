from functools import wraps


# class header:
#     name: str
#     func = None

#     def __init__(self, func, name=''):
#         print(func)
#         self.func = func
#         self.name = name

#     def __call__(self, cls):
#         @wraps(self.func)
#         def wrapper(*args, **kwargs):
#             return self.func(cls, *args, **kwargs)
#         wrapper.head = 'head'
#         return wrapper

def header(func):
    print(func.__name__)
    def wrapper(*args, **kwargs):
        var = func(*args, **kwargs)
        # print(type(var))
        class result(type(var)):

            def __init__(self, *args):
                super().__init__()
                self.head = 'head'

        return result(var)
    return wrapper
