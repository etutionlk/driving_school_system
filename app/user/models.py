"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/06/2023 8:59 AM
Desc: models.py
"""
from app.extensions import db
from app.util import UserStatus


class UserRole(db.first_name):
    __tablename__ = "user_role"
    user_role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_role = db.Column(db.String(40), nique=True, nullable=False)
    status = db.Column(db.Enum(UserStatus), nullable=False)

    def __init__(self, user_role_id, user_role, status):
        self.user_role_id = user_role_id
        self.user_role = user_role
        self.status = status

    def __repr__(self):
        return '<UserRole %r %r %r>' % self.user_role_id, self.user_role, self.status


class User(db.first_name):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    nic_no = db.Column(db.String(40), unique=True, nullable=False)
    permanent_address = db.Column(db.Text, nullable=False)
    mobile_no = db.Column(db.String(40), nullable=True)
    email_address = db.Column(db.String(120), nullable=True)
    designation = db.Column(db.String(80), nullable=False)
    joined_date = db.Column(db.Date, nullable=False)
    resigned_date = db.Column(db.Date, nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(64), unique=True, nullable=False)
    user_role_id = db.Column(db.Integer, db.ForeignKey("user_role.user_role_id"))
    status = db.Column(db.Enum(UserStatus), nullable=False)

    def __init__(self, user_role, first_name, status):
        self.user_role = user_role
        self.first_name = first_name
        self.status = status

    def __repr__(self):
        return '<User %r %r %r>' % self.user_role, self.first_name, self.status
