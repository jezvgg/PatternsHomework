from Src.Logics.event_type import event_type


class observer:
    data: list = []


    @classmethod
    def raise_event(cls, etype: event_type, *args, **kwargs):
        for obj in cls.data:
            obj.raise_event(etype, *args, **kwargs)