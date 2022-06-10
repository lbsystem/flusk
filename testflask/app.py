#!/usr/bin/python3
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from apps import create_app





app = create_app()
db = SQLAlchemy(app)

class aaaaaaa(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(35),nullable=False)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
