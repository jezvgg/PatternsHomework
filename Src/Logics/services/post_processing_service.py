from Src.Logics.services.abstract_service import abstract_service
from Src.Models.event_type import event_type
from Utils import logging
from Src.Models import *


class post_processing_service(abstract_service):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._events[event_type.delete_nomenculature()] = self.delete_nomenculature

    @logging
    def delete_nomenculature(self, obj: nomen_model):
        print(obj.name)
        for recipe in self.data:
            for row in recipe.rows:
                print(row.nomenculature.name)
                if row.nomenculature.name == obj.name:
                    print('smth')
                    recipe.rows.remove(row)
                    return True
        return False