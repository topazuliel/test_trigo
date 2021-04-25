from flask import Blueprint, jsonify, request, current_app

service_a_blueprint = Blueprint('/prod/service-a', __name__,url_prefix='')
SUCCESS = 'success'
FAILED = 'failed'


@service_a_blueprint.route('/prod/service-a/config', methods=['PUT'])
def update_config_file():
    data = request.json
    conf_name = data.pop('conf_name') if data.get('conf_name') else ''
    if not conf_name:
        return returned_json(status=FAILED, message="Can't fined any config to update check conf_name", rc=400)
    config_update = current_app.mongo.db.Prodconfig.find_one_and_update({'conf_name':conf_name},{'$set':data},upsert=False)
    if not config_update:
        return returned_json(status=FAILED, message="Can't update config", rc=400)
    return returned_json(status=SUCCESS, data='')

@service_a_blueprint.route('/dev/service-a/config', methods=['PUT'])
def update_dev_config_file():
    data = request.json
    conf_name = data.pop('conf_name') if data.get('conf_name') else ''
    if not conf_name:
        return returned_json(status=FAILED, message="Can't fined any config to update check conf_name", rc=400)
    config_update = current_app.mongo.db.Devconfig.find_one_and_update({'conf_name':conf_name},{'$set':data},upsert=False)
    if not config_update:
        return returned_json(status=FAILED, message="Can't update config", rc=400)
    return returned_json(status=SUCCESS, data='')

@service_a_blueprint.route('/prod/service-a/config', methods=['POST'])
def insert_config_file():
    data = request.json
    if current_app.mongo.db.Prodconfig.find_one({'conf_name':'service-a'}):
        return returned_json(status=FAILED, data='', message='config already inserted')
    config = current_app.mongo.db.Prodconfig.insert_one(data)
    return returned_json(status=SUCCESS, data='')

@service_a_blueprint.route('/dev/service-a/config', methods=['POST'])
def insert_dev_config_file():
    data = request.json
    if current_app.mongo.db.Devconfig.find_one({'conf_name':'service-a'}):
        return returned_json(status=FAILED, data='', message='config already inserted')
    config = current_app.mongo.db.Devconfig.insert_one(data)
    return returned_json(status=SUCCESS, data='')

@service_a_blueprint.route('/prod/service-a/config', methods=['GET'])
def get_config_file():
    c =[]
    config = current_app.mongo.db.Prodconfig.find_one({'conf_name':'service-a'},{'_id':0})
    if config:
        return returned_json(status=SUCCESS, data=config)
    return returned_json(status=FAILED, message="Can't fined any config", rc=400)

@service_a_blueprint.route('/dev/service-a/config', methods=['GET'])
def get_dev_config_file():
    c =[]
    config = current_app.mongo.db.Devconfig.find_one({'conf_name':'service-a'},{'_id':0})
    if config:
        return returned_json(status=SUCCESS, data=config)
    return returned_json(status=FAILED, message="Can't fined any config", rc=400)

def returned_json(status='', message='', data='', rc=200):
      return jsonify({'status':status, 'message':message, 'data': data}),rc