# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 16:29
# @Author  : DelayWu
# @Email   : DelayWu@163.com

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True, comment='')
    _password = Column(String(50))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
