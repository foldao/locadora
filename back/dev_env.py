from app import create_app
from model import *
app=create_app()
db.init_app(app)
app.app_context().push()
#     %run dev_env.py


#este arquivo é feito para ser executado em um notebook para manipular os bancos de dados via notebook em tempo de desenvolvimento

#this file is meant to be ran by a jupyter notebook so that the DB can be manipulated via notebook during development 