"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/06/2023 9:43 PM
Desc: models.py
"""
from app.extensions import db
from app.util import UserStatus


class UserRole(db.Model):
    __tablename__ = "user_role"
    user_role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_role = db.Column(db.String(40), unique=True, nullable=False)
    status = db.Column(db.Enum(UserStatus), nullable=False)

    def __init__(self, user_role_id, user_role, status):
        self.user_role_id = user_role_id
        self.user_role = user_role
        self.status = status

    def __repr__(self):
        return '<UserRole %r %r %r>' % self.user_role_id, self.user_role, self.status