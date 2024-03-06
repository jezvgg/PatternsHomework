from Src.Logics.report import report
from Utils import typecheck
import json


class report_json(report):

    @typecheck(expression=lambda x: x['storage_key'])
    def create(self, storage_key: str):
        result = []
        for model in self._storage.data[storage_key]:
            result.append({str(key):str(value) for key, value in model.get_by_attr('head').items()})
        return json.dumps(result)