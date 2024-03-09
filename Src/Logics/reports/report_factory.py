from Src.Logics.reports.report_csv import report, report_csv
from Src.Logics.reports.report_markdown import report_markdown
from Src.Logics.reports.report_json import report_json
from Src.exeptions import operation_exception
from Src.Storage.storage import storage
from Utils import typecheck


class report_factory:
    __maps: dict = {}


    def __init__(self):
        self.__build_structure()


    def __build_structure(self):
        self.__maps['csv'] = report_csv
        self.__maps['markdown'] = report_markdown
        self.__maps['json'] = report_json


    @typecheck(expression=lambda x: x['storage'])
    def create(self, format: str, storage: storage) -> report:
        
        if format not in self.__maps.keys():
            raise operation_exception("Нет подходящего обработчика")

        return self.__maps[format](storage)