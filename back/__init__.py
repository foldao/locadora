from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/teste.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key='bean legalzaum'
    return app