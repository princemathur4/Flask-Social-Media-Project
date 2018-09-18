from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user ={"username":"Prince Mathur"}
    return render_template('index2_1.html',title="Home",user=user)
