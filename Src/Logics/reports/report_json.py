from Src.Logics.reports.report import report
from Src.Logics.reports.converter import convert_factory
from Utils import typecheck
import json


class report_json(report):

    @typecheck(expression=lambda x: x['storage_key'])
    def create(self, storage_key: str):
        result = []
        for model in self._storage.data[storage_key]:
            result.append({str(key):convert_factory.create(value).convert(value) for key, value in model.get_by_attr('head').items()})
        return json.dumps(result, indent=4, ensure_ascii=False)


    def load(self, data: dict, dtype: type):
        pass
        