from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)   #instance
app.config.from_object(Config)

db= SQLAlchemy(app)
migrate= Migrate(app,db)

login = LoginManager(app)
login.login_view = 'login'    # name you would use in "url_for" call to get the url

# from app import routes5_1, models 
from app import routes6_1, models

if(__name__=='__main__'):
    app.run()
