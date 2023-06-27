"""
Name : models.py
Author : Chinthaka Maduranga
Contact : chinthaka.maduranga@blackswan-technologies.com
Time : 09/04/2023 6:48 PM
Desc: models
"""
from app.extensions import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r %r>' % self.username, self.email
