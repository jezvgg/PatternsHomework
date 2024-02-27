from Src.Logics.report import report
from Utils.typecheck import typecheck
import inspect


class report_csv(report):

    @typecheck
    def create(self, storage_key: str):
        print(list(filter(lambda x: not x[0].startswith('_') and not inspect.ismethod(x[1]),inspect.getmembers(self._storage.data[storage_key][0]))))

        
        return list(filter(lambda x: not x.startswith('_'),dir(self._storage.data[storage_key][0])))
