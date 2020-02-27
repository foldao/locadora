from flask_restplus import Api

from .users import api as users

api = Api(
    title='API',
    version='1.0',
    description='Casca de Api',
    # All API metadatas
)

api.add_namespace(users)