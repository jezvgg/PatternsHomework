from Src.Logics.reports.report import report
from Utils import typecheck


class report_markdown(report):

    @typecheck(expression=lambda x: x['storage_key'])
    def create(self, storage_key: str):
        result = []
        headers = self._storage.data[storage_key][0].get_attr_keys('head')
        result.append('| '+" | ".join(headers)+' |')
        result.append('|'+"|".join(['-' for _ in range(len(headers))]) +'|')
        for model in self._storage.data[storage_key]:
            result.append('| '+' | '.join(map(str, model.get_attr_values('head')))+' |')
        return '\n'.join(result)