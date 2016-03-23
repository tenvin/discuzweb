#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)

db = SQLAlchemy()
db.init_app(app)

bootstrap = Bootstrap(app)


from app.database import db_session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

from app.views  import *



