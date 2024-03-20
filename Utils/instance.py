def instance_checker(obj, dtype: type):
    if hasattr(dtype, '__origin__'):
        return all([instance_checker(obj, dtype.__origin__), 
        all([instance_checker(x, dtype.__args__) for x in obj])])
    return isinstance(obj, dtype)