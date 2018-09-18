from flask import Flask
from config import Config

app = Flask(__name__)   #instance
app.config.from_object(Config)
# from app import routes
# from app import routes1_1
# from app import routes2_1
# from app import routes2_2
from app import routes2_3

if(__name__=='__main__'):
    app.run()
    