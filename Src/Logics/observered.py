from Src.Logics.observer import observer
from Src.Logics.event_type import event_type


class observered:
    _events = {}


    def __init__(self):
        observer.data.append(self)


    def raise_event(self, etype: event_type, *args, **kwargs):
        if etype not in self._events.keys(): return
        self._events[etype](*args, **kwargs)