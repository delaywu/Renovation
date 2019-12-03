# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 11:49
# @Author  : DelayWu
# @Email   : DelayWu@163.com

import sqlalchemy

print(sqlalchemy.__version__)

from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine('sqlite:///:memory', echo=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

session.add(ed_user)
session.commit()

our_user = session.query(User).filter_by(name='ed').first()

print(our_user)
