from Src.Logics.reports.converter import convertor
from Utils import typecheck, AttrWorker

class convertor_models(convertor):

    @staticmethod
    @typecheck
    def convert(obj: AttrWorker):
        from Src.Logics.reports.converter import convert_factory
        return {key:convert_factory.create(value).convert(value) for key, value in obj.get_by_attr('head').items()}