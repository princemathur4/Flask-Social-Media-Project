from flask import Flask

app = Flask(__name__)   #instance
from app import routes