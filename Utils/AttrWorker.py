from Utils.attribute import attribute


class AttrWorker:

    def getattrs(self) -> tuple:
        attributes = set([])
        for method in dir(type(self)):
            if isinstance(getattr(type(self), method), attribute):
                attributes |= set(dir(getattr(type(self), method))) ^ set(dir(attribute))
        return attributes

    def get_by_attr(self, attr: str) -> dict:
        result = {}
        for method in dir(type(self)):
            if hasattr(getattr(type(self), method), attr):
                result[getattr(getattr(type(self), method), attr)] = getattr(self, method)
        return result

    def get_attr_keys(self, attr: str) -> list:
        return list(self.get_by_attr(attr).keys())

    def get_attr_values(self, attr: str) -> list:
        return list(self.get_by_attr(attr).values())

    