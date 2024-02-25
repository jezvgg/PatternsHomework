from typing import Union

def instance_checker(obj, dtype: type):
    if hasattr(dtype, '__origin__'):
        return all([instance_checker(obj, dtype.__origin__), 
        all([instance_checker(x, dtype.__args__) for x in obj])])

    return isinstance(obj, dtype)

print(instance_checker([1,2,3], list[int]))
