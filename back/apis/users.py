from flask_restplus import Namespace, Resource
api=Namespace('users', description='funções relacionadas a usuários')
@api.route('/teste')
class Teste(Resource):
    def get(self):
        return {'msg':'lol'}, 200