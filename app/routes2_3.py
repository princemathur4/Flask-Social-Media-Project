<<<<<<< HEAD
from flask import render_template,flash,redirect,url_for
from app import app
from app.forms import LoginForm
=======
<<<<<<< HEAD
from flask import render_template
from app import app

=======
from flask import render_template,flash,redirect,url_for
from app import app
from app.forms import LoginForm
>>>>>>> chapter3
>>>>>>> 7df3c437a99e9ed318de3c8ce9a6ab21806845e2
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 7df3c437a99e9ed318de3c8ce9a6ab21806845e2

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        flash(f'Login requested for user {form.username.data}, remember_me = {form.remember_me.data}')
        return redirect(url_for('index'))
<<<<<<< HEAD
    return render_template('login.html',title='Sign in',form=form)
=======
    return render_template('login.html',title='Sign in',form=form)
>>>>>>> chapter3
>>>>>>> 7df3c437a99e9ed318de3c8ce9a6ab21806845e2
