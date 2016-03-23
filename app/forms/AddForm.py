#!/usr/bin/env python
#-*- coding:utf-8 -*-


from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired,URL

class AddForm(Form):
    url = StringField('url',validators=[DataRequired(),URL()])
    user = StringField('user',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])