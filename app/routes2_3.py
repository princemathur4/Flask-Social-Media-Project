from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user ={"username":"Prince"}
    posts=[
        {
            'author':{"username":"Aditya"},
            'body':'Beautiful day in New york'
        },
        {
            'author':{'username':'Ishan'},
            'body':'The Avengers is the best movie ever!'
        }
    ]
    return render_template('index2_3.html',title="Home",user=user,posts=posts)
