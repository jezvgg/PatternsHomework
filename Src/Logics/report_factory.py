from Src.Logics.report_csv import report, report_csv
from Src.exeptions import operation_exception
from Src.Storage.storage import storage
from Utils import typecheck


class report_factory:
    __maps: dict = {}


    def __init__(self):
        self.__build_structure()


    def __build_structure(self):
        self.__maps['csv'] = report_csv


    @typecheck(expression=lambda x: x['storage'])
    def create(self, format: str, storage: storage) -> report:
        
        if format not in self.__maps.keys():
            raise operation_exception("Нет подходящего обработчика")

        return self.__maps[format](storage)