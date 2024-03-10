from Src.Logics.reports.converter import convertor


class convertor_iterator(convertor):

    @staticmethod
    def convert(obj):
        from Src.Logics.reports.converter import convert_factory
        return [convert_factory.create(value).convert(value) for value in obj]