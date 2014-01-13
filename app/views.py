from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ang'} # fake user
    posts = [ # fake array of posts
              {
                'author' : {'nickname' : 'Ang'},   
                'body' : 'Beautiful day in Ireland!'
              }, 
              {
                'author' : {'nickname' : 'Gao'},   
                'body' : 'Hacking a blog'
              } 
            ]
    return render_template('index.html', 
            title = 'Home', 
            user=user,
            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requestede for OpendID=' + form.openid.data + ', remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
            title = 'Sign In',
            form = form,
            providers = app.config['OPENID_PROVIDERS'])
