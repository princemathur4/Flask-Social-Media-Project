import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-aint-telling-you-shit'
    print(SECRET_KEY)