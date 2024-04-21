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

    def get_by_attr(self, attr: str, obj_type: type = None) -> dict:
        result = {}
        for method in dir(self):
            if hasattr(getattr(self, method), attr):
                result[getattr(getattr(self, method), attr)] = getattr(self, method)
        return result

    def get_attr_keys(self, attr: str) -> list:
        return list(self.get_by_attr(attr).keys())

    def get_attr_values(self, attr: str) -> list:
        return list(self.get_by_attr(attr).values())

    