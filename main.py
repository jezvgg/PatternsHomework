from flask import Flask
from Src.Logics.report_factory import report_factory
from Src.settings_manager import settings_manager
from Src.Logics.start_factory import start_factory


app = Flask(__name__)


@app.route('/api/report/<storage_key>', methods=['GET'])
def get_report(storage_key: str):

    manager = settings_manager()
    start = start_factory(manager.settings)
    factory = report_factory()
    report = factory.create(manager.settings.report_format, start.storage)

    if storage_key not in start.storage.data.keys():
        return "Такого ключа нет", 500

    data = report.create(storage_key)

    response = app.response_class(
        response=data,
        status=200,
        mimetype="application/text"
    )
    return response

if __name__ == "__main__":
    app.run()