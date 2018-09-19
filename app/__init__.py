from flask import Flask
from config import Config
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)   #instance
app.config.from_object(Config)

db= SQLAlchemy(app)
migrate= Migrate(app,db)

=======

app = Flask(__name__)   #instance
<<<<<<< HEAD
=======
app.config.from_object(Config)
>>>>>>> chapter3
>>>>>>> 7df3c437a99e9ed318de3c8ce9a6ab21806845e2
# from app import routes
# from app import routes1_1
# from app import routes2_1
# from app import routes2_2
<<<<<<< HEAD
from app import routes2_3,models

if(__name__=='__main__'):
    app.run()
    
=======
from app import routes2_3

if(__name__=='__main__'):
    app.run()
<<<<<<< HEAD
=======
    
>>>>>>> chapter3
>>>>>>> 7df3c437a99e9ed318de3c8ce9a6ab21806845e2
