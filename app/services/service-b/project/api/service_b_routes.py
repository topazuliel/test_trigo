from flask import Blueprint, jsonify, request, current_app
SUCCESS = 'success'
FAILED = 'failed'
service_b_blueprint = Blueprint('/prod/service-b', __name__,url_prefix='')

@service_b_blueprint.route('/prod/service-b/config', methods=['GET'])
def get_config_file():
    c =[]
    config = current_app.mongo.db.Prodconfig.find({},{'_id':0})
    for conf in config:
        c.append(conf)
    if c:
        return returned_json(status=SUCCESS, data=conf)
    return returned_json(status=FAILED, message="Can't fined any config", rc=400)

def returned_json(status='', message='', data='', rc=200):
      return jsonify({'status':status, 'message':message, 'data': data}),rc