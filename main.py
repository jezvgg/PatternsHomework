from Src.Logics.reports.report_factory import report_factory
from Src.Logics.services import storage_service, nomenculature_service
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

    factory = report_factory()
    report = factory.create(options.settings.report_format, start.storage)

    if storage_key not in start.storage.data.keys():
        return "Такого ключа нет", 500

    data = report.create(storage_key)

    result = app.response_class(
            response = data,
            status=200,
            mimetype="application/json; charset=utf-8"
        )
    return result


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

@app.route('/api/storage/<nomenculature_id>/turns')
def get_nomens_rests(nomenculature_id):
    nomens = [nomen for nomen in start.storage.data[storage.nomenculature_key()] if nomen.id == nomenculature_id]

    if not nomens:
        raise operation_exception("Нет подходяших  данных!")

    nomen = nomens[0]

    service = storage_service(start.storage.data[storage.journal_key()])
    result = service.create_turns( nomen )

    return storage_service.create_response(result, app)

@app.route('/api/storage/<recipe_id>/debits')
def debits_recipe(recipe_id):
    args = request.args
    if 'storage_id' not in args:
        raise operation_exception("Не указан склад!")

    recipes = [recipe for recipe in start.storage.data[storage.recipe_key()] if recipe.id == recipe_id]
    storages_ = [storage for storage in start.storage.data[storage.storages_key()] if storage.id == args['storage_id']]

    if not recipes or not storages_:
        raise operation_exception("Нет подходяших  данных!")

    recipe = recipes[0]
    storage_ = storages_[0]

    start.storage.data[storage.journal_key()] += storage_service(start.storage.data[storage.journal_key()]).create_debits(recipe, storage_)

    return storage_service.create_response({'success': True}, app)

@app.route('/api/storage/<nomenculature_id>/list', methods=['GET'])
def get_nomens_list(nomenculature_id):
    nomens = [nomen for nomen in start.storage.data[storage.nomenculature_key()] if nomen.id == nomenculature_id]

    args = request.args
    storage_ = None
    if 'storage' in args.keys() and args['storage']: storage_ = args['storage']

    if not nomens:
        raise operation_exception("Нет подходяших  данных!")

    nomen = nomens[0]

    service = storage_service(start.storage.data[storage.journal_key()])
    result = service.create_turns( nomen, storage=storage_ )

    return storage_service.create_response(result, app)


@app.route('/api/get_nomenculature/<nomen_id>', methods=['GET'])
def get_nomenculature(nomen_id):
    nomen_service = nomenculature_service(start.storage.data[storage.nomenculature_key()])
    result = nomen_service.get_nomenculature(nomen_id)

    return nomenculature_service.create_response(result, app)


@app.route('/api/del_nomenculature/<nomen_id>', methods=['DELETE'])
def del_nomenculature(nomen_id):
    nomen_service = nomenculature_service(start.storage.data[storage.nomenculature_key()])
    result = nomen_service.del_nomenculature(nomen_id)

    return nomenculature_service.create_response(result, app)


@app.route('/api/add_nomenculature', methods=['POST'])
def add_nomenculature():
    nomen_json = request.json
    nomen_service = nomenculature_service(start.storage.data[storage.nomenculature_key()])
    result = nomen_service.add_nomenculature(nomen_json)

    return nomenculature_service.create_response(result, app)


@app.route('/api/patch_nomenculature/<nomen_id>', methods=['PATCH'])
def patch_nomenculature(nomen_id):
    nomen_json = request.json

    nomen_service = nomenculature_service(start.storage.data[storage.nomenculature_key()])
    result = nomen_service.change_nomenculature(nomen_id, nomen_json)

    return nomenculature_service.create_response(result, app)


@app.route('/api/change_block_period', methods=['GET'])
def change_block_period():

    args = request.args
    if 'block_period' in args:
        options.settings.block_period = datetime.strptime(args['block_period'], '%Y-%m-%d')
    rern = options.save()

    result = app.response_class(
            response = rern,
            status=200,
            mimetype="application/json; charset=utf-8"
        )
    return result


if __name__ == "__main__":
    app.run()