from flask_restplus import Api, Resource
from __init__ import create_app
API=Api()
@API.route('/teste')
class Teste(Resource):
    def get(self):
        return {'msg':'lol'}, 200