from Src.Logics.report import report
from Utils.typecheck import typecheck
import inspect


class report_csv(report):

    @typecheck
    def create(self, storage_key: str):

        obj = self._storage.data[storage_key][0]
        for x in dir(obj):
            if not x.startswith('_'):
                # print(x)
                # print(getattr(obj, x))
                #print(hasattr(getattr(obj, x), 'head'))
                #print('\n',x)
                #print('value:',getattr(obj, x))
                #print(type(getattr(obj, x)))
                if hasattr(getattr(obj, x), 'head'):
                    print('\n',x)
                    print('value:',getattr(obj, x))
                    print('name:',getattr(getattr(obj, x), 'head'))
                pass

        print(self._storage.data[storage_key][0].coef)
 