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
        cls = self
        if not isinstance(self, type): cls = type(self)
        result = {}
        for method in dir(cls):
            if hasattr(getattr(cls, method), attr):
                result[getattr(getattr(cls, method), attr)] = getattr(self, method)
        return result

    def get_attr_keys(self, attr: str) -> list:
        return list(self.get_by_attr(attr).keys())

    def get_attr_values(self, attr: str) -> list:
        return list(self.get_by_attr(attr).values())

    