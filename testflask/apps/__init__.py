#!/usr/bin/python3
from flask import Flask
from redis import Redis
class Config:
    SECRET_KEY = "dadasfgafdaf"

    RECAPTCHA_PUBLIC_KEY="fasdfasdfsadfasdfas"
    SESSION_TYPE= 'redis'
    SESSION_REDIS = Redis(host='192.168.1.32', port=6379, db=7, password='p34mv160')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:p34mv160@192.168.1.32:3306/testbase?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    return app
