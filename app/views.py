#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, request, redirect, url_for, abort, \
     render_template, flash

from app.forms.AddForm import AddForm
from app.forms.LoginForm import LoginForm
from . import app, db
from app.models.Url import Url

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add')
def add():
    entries = db.session.query(Url).all()
    return render_template('add.html', entries=entries)

@app.route('/add2',methods=['GET', 'POST'])
def add2():
    entries = db.session.query(Url).all()

    form = AddForm()
    if form.validate_on_submit():
        if request.method == 'POST':

            item = Url(url=form.url.data,
                       username=form.user.data,
                       password=form.password.data
            )
            db.session.add(item)
            db.session.commit()

        return redirect(url_for('add2'))

    return render_template('add2.html', form=form, entries=entries)

@app.route('/hello/')
def hello():
    return render_template('hello.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route("/add_action",methods=['GET', 'POST'])
def add_entry():
    error = None
    if request.method == 'POST':
        url,usr,password = request.form['url'], request.form['username'],request.form['password']
        item = Url(url,usr,password)
        db.session.add(item)
        db.session.commit()
        flash('New entry was successfully posted')

    return redirect(url_for('add2'))
