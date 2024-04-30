from Src.Logics.services.abstract_service import abstract_service
from Src.Logics.event_type import event_type
from Src.Logics.reports.converter import convert_factory
from Src.proxy import event_proxy
import json


class logging_service(abstract_service):
    __first_append = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__first_append = True
        self._events[event_type.add_log()] = self.create_log
        self._events[event_type.create_log()] = self.create_log_file

    
    def create_log_file(self):
        with open('logs.json', 'w') as f:
            f.write('[\n]')


    def create_log(self, event: event_proxy):
        if event in self.data: return
        self.data.append(event)
        log = json.dumps(convert_factory.create(event).convert(event), indent=4, ensure_ascii=False)+'\n]'
        if not self.__first_append: log = ','+log
        with open('logs.json', 'rb+') as f:
            f.seek(-1, 2)
            f.write(log.encode())
        self.__first_append = False
