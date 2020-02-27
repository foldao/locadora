from flask_cors import CORS
from flask import Flask
from model import db
from apis import api
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/teste.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key='bean legalzaum'
    return app
if __name__ == "__main__":
    app=create_app()
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    api.init_app(app)
    db.init_app(app)    
    app.run(debug=True)