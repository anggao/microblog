#!flask/bin/python
import os
os.environ['DATABASE_URL'] = 'mysql://apps:apps@localhost/apps'

from flup.server.fcgi import WSGIServer
from app import app

if __name__ == '__main__':
    WSGIServer(app).run()
