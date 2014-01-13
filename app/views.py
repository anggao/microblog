from flask import render_template
from app import app

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
