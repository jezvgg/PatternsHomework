from Src.Models.event_type import event_type


class observer:
    data: list = []


    @classmethod
    def raise_event(cls, etype: event_type):
        for obj in cls.data:
            obj.raise_event(etype)