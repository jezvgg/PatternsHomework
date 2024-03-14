from Src.Logics.processes.abstract_process import abstract_process
from Src.Models import storage_turn_model


class process_storage_turn(abstract_process):
    
    def create(self):
        result = {}
        for transaction in self._journal:
            key = (transaction.nomenculature, transaction.storage, transaction.unit.to_base)
            value = transaction.counts * self.operations[transaction.opearation]
            if key not in result.keys():
                result[key] = value
            else:
                result[key] += value

        turns = []
        for key, value in result.items():
            turn = storage_turn_model(storage_=key[1], remains=value, nomen=key[0], unit=key[2])
            turns.append(turn)

        return turns