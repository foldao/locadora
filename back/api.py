from flask_restplus import Api, Resource
API=Api()
@API.route('/teste')
class Teste(Resource):
    def get(self):
        return {'msg':'lol'}, 200