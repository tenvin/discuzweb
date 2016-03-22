#!/usr/bin/env python
#-*- coding:utf-8 -*-
from app.database import Base
from sqlalchemy import Column, Integer, String


class Url(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True,autoincrement=True)
    url = Column(String(100))
    username = Column(String(20))
    password = Column(String(20))

    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password

    def __repr__(self):
        return '<url %r>' % (self.url)

