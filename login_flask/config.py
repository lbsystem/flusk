#!/usr/bin/python3
from flask import Flask,request,make_response,render_template,redirect,url_for,abort,session
from flask_bootstrap import Bootstrap
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

class Config:
    SECRET_KEY = "dadasfgafdaf"

    RECAPTCHA_PUBLIC_KEY="fasdfasdfsadfasdfas"
    SESSION_TYPE= 'redis'
    SESSION_REDIS = Redis(host='192.168.1.32', port=6379, db=2, password='p34mv160')
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:p34mv160@192.168.1.32:3306/BGPDATA?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

app=Flask(__name__)

app.config.from_object(Config)
db=SQLAlchemy(app)
Session(app)
bootstrap = Bootstrap(app)

def login_required(func):
    def wrapper(*args,**kwargs):
        if session.get("name") is None:
            abort(401)
        else:
            return func(*args,**kwargs)
    return wrapper


class Alchermy:
    def __init__(self):
        engine = create_engine('mysql+pymysql://root:p34mv160@192.168.1.32:3306/movie?charset=utf8',
                               max_overflow=0,
                               pool_size=5,
                               pool_timeout=30,
                               pool_recycle=1
                               )
        self.Base = automap_base()
        self.Base.prepare(engine, reflect=True)
        self.movie= self.Base.classes.movie
        self.session = Session(engine)

    def sql(self,name):
        return  self.session.query(self.movie).filter_by(name=name).one()

