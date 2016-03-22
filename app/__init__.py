#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('../config.py')
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)

db = SQLAlchemy()
db.init_app(app)

from app.database import db_session
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()



