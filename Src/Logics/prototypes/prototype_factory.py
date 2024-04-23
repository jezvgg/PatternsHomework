from Src.Logics.prototypes import *
from Src.Models import *


class prototype_factory:
    __maps = {
        storage_transaction_model: storage_prototype
    }
    prototype = None

    @classmethod
    def create(cls, dtype):
        return cls.__maps[dtype]

    def __init__(self, data):
        self.prototype = prototype_factory.create(type(data[0]))(data)

    
    def filter_by(self, filter_model):
        return self.prototype.filter_by(filter_model)
