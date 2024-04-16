from Utils.attribute import attribute


class AttrWorker:

    @classmethod
    def getattrs(cls, obj_type=None) -> tuple:
        if obj_type is None: obj_type = cls
        attributes = set([])
        for method in dir(obj_type):
            if isinstance(getattr(obj_type, method), attribute):
                attributes |= set(dir(getattr(obj_type, method))) ^ set(dir(attribute))
        return attributes

    @classmethod
    def get_by_attr(cls, attr: str, obj_type: type = None) -> dict:
        result = {}
        for method in dir(cls):
            if hasattr(getattr(cls, method), attr):
                result[getattr(getattr(cls, method), attr)] = getattr(cls, method)
        return result

    @classmethod
    def get_attr_keys(cls, attr: str) -> list:
        return list(cls.get_by_attr(attr).keys())

    @classmethod
    def get_attr_values(cls, attr: str) -> list:
        return list(cls.get_by_attr(attr).values())

    