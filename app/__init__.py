from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)   #instance
app.config.from_object(Config)

db= SQLAlchemy(app)
migrate= Migrate(app,db)

# from app import routes
# from app import routes1_1
# from app import routes2_1
# from app import routes2_2
from app import routes2_3,models

if(__name__=='__main__'):
    app.run()
    