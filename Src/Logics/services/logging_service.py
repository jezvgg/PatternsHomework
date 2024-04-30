from Src.Logics.services.abstract_service import abstract_service
from Src.Models.event_type import event_type
from Src.Logics.reports.converter import convert_factory
from Src.proxy import event_proxy
import json


class logging_service(abstract_service):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._events[event_type.add_log()] = self.create_log


    def create_log(self, event: event_proxy):
        self.data.append(event)
        log = (json.dumps(convert_factory.create(event).convert(event), indent=4, ensure_ascii=False)+',').encode()
        with open('logs.json', 'rb+') as f:
            f.seek(-11, 2)
            f.write(log)
            f.write(b'\n"Logs end"]')
