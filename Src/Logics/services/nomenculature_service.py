import uuid
from Src.Models import *
from Src.Logics.observer import observer
from Src.Logics.services import abstract_service
from Src.Logics.reports.converter import deconvertor
from Src.Logics.prototypes import nomenculature_prototype


class nomenculature_service(abstract_service):

    def add_nomenculature(self, nomen_json: dict) -> bool:
        nomenculature = deconvertor().deserialize(nomen_json, nomen_model)
        self._data.append(nomenculature)
        return True

    def get_nomenculature(self, nomen_id: str) -> nomen_model:
        nomen = nomenculature_prototype(self._data).filter_by(uuid.UUID(nomen_id))
        if nomen:
            return nomen[0]
        return False

    def del_nomenculature(self, nomen_id: str) -> bool:
        nomen = nomenculature_prototype(self._data).filter_by(uuid.UUID(nomen_id))
        if nomen:
            observer.raise_event(event_type.delete_nomenculature(), nomen[0])
            self._data.remove(nomen[0])
            return True
        return False

    def change_nomenculature(self, nomen_id: str, new_nomen_json: dict) -> bool:
        de = self.del_nomenculature(nomen_id=nomen_id)
        add = self.add_nomenculature(new_nomen_json)
        print(de ,add)
        return all([de, add])