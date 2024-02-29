from Src.Logics.report import report
from Utils import typecheck, attribute


class report_csv(report):

    @typecheck
    def create(self, storage_key: str):

        for obj in self._storage.data[storage_key]:
            for x in dir(type(obj)):
                if hasattr(getattr(type(obj), x), 'head'):
                    print('\n', x)
                    print('value:',getattr(obj, x))
                    print('head:',getattr(getattr(type(obj), x), 'head'))
                