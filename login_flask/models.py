#!/usr/bin/python3
from config import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(35),unique=True,nullable=False)
    password = db.Column(db.String(35),nullable=False)
    email = db.Column(db.String(64),unique=True,nullable=False)

    def __str__(self):
        return 'User: %s' % self.username

