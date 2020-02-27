from flask_cors import CORS
from __init__ import create_app
from model import db
from api import API

app=create_app()
app.app_context().push()
if __name__ == "__main__":
    db.create_all()
    API.init_app(app)
    db.init_app(app)    
    app.run()