import os 
<<<<<<< HEAD
basedir =os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-aint-telling-you-shit'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+ os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-aint-telling-you-shit'
    print(SECRET_KEY)
>>>>>>> 7df3c437a99e9ed318de3c8ce9a6ab21806845e2
