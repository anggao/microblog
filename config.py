# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLE = True
SECRET_KEY = 'my-key'

OPENID_PROVIDERS = [
{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},        
{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},        
{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},        
{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},        
{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

# mail server settings
#MAIL_SERVER = 'localhost'
#MAIL_PORT = 25
#MAIL_USERNAME = None
#MAIL_PASSWORD = None
MAIL_SERVER = 'smtp.mail.yahoo.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'ang_gao@yahoo.com'
MAIL_PASSWORD = ''

# administrator list
ADMINS = ['ang_gao@yahoo.com']

# pagination
POSTS_PER_PAGE = 3

# Whoosh configuration
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

LANGUAGES = {
'en': 'English',        
'zh': '中文'
}

# microsft translation service
MS_TRANSLATOR_CLIENT_ID = "anggao" 
MS_TRANSLATOR_CLIENT_SECRET = "44ZXrN3yLZyGwt5IQO9BtvdM4F37tfMC2k0a99EXb7Y=" 

SQLALCHEMY_RECORD_QUERIES = True

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5
