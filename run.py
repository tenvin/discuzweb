#!/usr/bin/env python
#coding=utf-8
#from flask.ext.script import Manager, Shell, Server

#from app import create_app

#manager = Manager(create_app('config.cfg'))

#manager.add_command("runserver", Server('0.0.0.0',port=5000))
from flask import Flask

from app import app

from app.routes  import *

if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)