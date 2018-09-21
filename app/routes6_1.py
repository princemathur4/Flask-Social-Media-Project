from flask import render_template,flash,redirect,url_for
from app import app,db
from app.forms import LoginForm,RegistrationForm,EditProfileForm
from app.models import User
from flask_login import login_required,login_user,logout_user,current_user
from flask import request
from werkzeug.urls import url_parse
from time import sleep
from datetime import datetime


@app.before_request
def before_request():
    print("Current user: ",current_user)
    if current_user.is_authenticated:
        current_user.last_seen =datetime.utcnow()
        db.session.commit()

@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form=EditProfileForm()
    if form.validate_on_submit():
        u=User.query.filter_by(username=form.username.data).one_or_none()
        if(u is not None):
            current_user.username= form.username.data
        else:
            flash("This username is taken.\n Try another one.")
        current_user.about_me= form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html',title='Edit Profile', form=form)

@app.route('/')
@app.route('/index')
def index():
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
    return render_template('index5_1.html',title="Home Page",posts=posts)

@app.route('/users/<username>')
@login_required
def users(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts=[
        {
            'author':user,
            'body':'Test post #1'
        },
        {
            'author':user,
            'body':'Test post #2'
        }
    ]
    return render_template('users.html',user=user,posts=posts)

@app.route('/about')
def about():
    abt={
            'Creator':"Miguel Grinberg",
            'Purpose':'Designed for Students'
        }
    return render_template('about.html',abt=abt)


@app.route('/login', methods=['GET','POST'])
def login():
    print(current_user)
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if((user is None) or (not user.check_password(form.password.data))):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user,remember=form.remember_me.data)
        # return redirect(url_for('index'))
        next_page= request.args.get('next')
        if ((not next_page) or (url_parse(next_page).netloc!= '')):
            next_page= url_for('index')
        return redirect(next_page)
    return render_template('login.html',title='Sign in',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    
    if form.is_submitted():
        print("Submitted Successfully!")
    if form.validate():
        print("Validated")
    print(form.errors)

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Awesome, you\'re all set up!')
        sleep(3)
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
