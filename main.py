from Src.Logics.reports.report_factory import report_factory
from Src.Logics.storage_service import storage_service
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.exeptions import operation_exception
from Src.Storage.storage import storage
from flask import Flask, request
from datetime import datetime
from Src.Models import *



app = Flask(__name__)
options = settings_manager()
start = start_factory(options.settings)
start.create()

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

@app.route('/api/report/rests', methods = ['GET'])
def get_rests():
    args = request.args
    if 'start_period' not in args.keys() or 'stop_period' not in args.keys():
        raise operation_exception("Нет дат!")

    start_date = datetime.strptime(args['start_period'], '%Y-%m-%d')
    stop_date = datetime.strptime(args['stop_period'], '%Y-%m-%d')

    service = storage_service(start.storage.data[storage.journal_key()])
    result = service.create_turns(period(start=start_date, end=stop_date))

    return storage_service.create_response(result, app)


if __name__ == "__main__":
    app.run()