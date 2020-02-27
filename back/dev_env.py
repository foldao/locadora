from __init__ import create_app
from model import *
app=create_app()
db.init_app(app)
app.app_context().push()
#     %run dev_env.py