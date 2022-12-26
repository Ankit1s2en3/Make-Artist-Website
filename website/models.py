from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    userId = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(150))

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    phone = db.Column(db.Integer)
    email = db.Column(db.String(500))
    name = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
