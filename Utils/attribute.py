

class attribute(property):

    def __init__(self, func = None, *args, **kwargs,):
        
        for attr in kwargs.keys():
            print(attr, kwargs[attr])
            setattr(self, attr, kwargs[attr])

        if func is not None:
            super().__init__(func, *args)


    def __call__(self,func):
        self.__init__(func)
        return self


    def setter(self, fset):
        kwargs = {x:getattr(self, x) for x in set(dir(self)) ^ set(dir(attribute))}
        return type(self)(self.fget, fset, self.fdel, self.__doc__, **kwargs)
        
