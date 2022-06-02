#!/usr/bin/python3
from flask import Flask,request,make_response,render_template
from flask_bootstrap import Bootstrap
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import Redis


class Config:
    SECRET_KEY = "dadasfgafdaf"

    RECAPTCHA_PUBLIC_KEY="fasdfasdfsadfasdfas"
    SESSION_TYPE= 'redis'
    SESSION_REDIS = Redis(host='192.168.1.32', port=6379, db=2, password='p34mv160')
    SQLALCHEMY_DATABASE_URI="sqlite:////sql/login_flask.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

app=Flask(__name__)

app.config.from_object(Config)
db=SQLAlchemy(app)
Session(app)
bootstrap = Bootstrap(app)



