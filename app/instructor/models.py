"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 29/06/2023 11:23 PM
Desc: models.py
"""
from app.extensions import db
from app.util import Status


class Instructor(db.Model):
    __tablename__ = "instructor"
    instructor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    driving_licence_number = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)

    def __init__(self, instructor_id, user_id):
        self.instructor_id = instructor_id
        self.user_id = user_id

    def __repr__(self):
        return '<Instructor %r %r>' % self.instructor_id, self.user_id
