#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, request, redirect, url_for, abort, \
     render_template, flash

from app import app, db
from app.models.url import Url

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add')
def show_entries():
    entries = db.session.query(Url).all()
    return render_template('add.html', entries=entries)

@app.route('/hello/')
def hello():
    return render_template('hello.html')

@app.route("/add_action",methods=['GET', 'POST'])
def add_entry():
    error = None
    if request.method == 'POST':
        url,usr,password = request.form['url'], request.form['username'],request.form['password']
        item = Url(url,usr,password)
        db.session.add(item)
        db.session.commit()
        flash('New entry was successfully posted')

    return redirect(url_for('show_entries'))
