from Src.Logics.reports.converter import convertor
from datetime import datetime
from Utils import typecheck


class convertor_datetime(convertor):

    @staticmethod
    @typecheck
    def convert(obj: datetime):
        return {"Год":obj.year,
                "Месяц":obj.month,
                "День":obj.day,
                "Час":obj.hour,
                "Минуты":obj.minute,
                "Секунды":obj.second}