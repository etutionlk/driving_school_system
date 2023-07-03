"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/06/2023 8:59 AM
Desc: models.py
"""
from app.extensions import db
from app.util import UserStatus
from app.util.constants import CASCADE


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    nic_no = db.Column(db.String(40), unique=True, nullable=False, index=True)
    permanent_address = db.Column(db.Text, nullable=False)
    mobile_no = db.Column(db.String(40), nullable=True)
    email_address = db.Column(db.String(120), nullable=True, index=True)
    designation = db.Column(db.String(80), nullable=False)
    joined_date = db.Column(db.Date, nullable=False)
    resigned_date = db.Column(db.Date, nullable=True)
    username = db.Column(db.String(60), unique=True, nullable=False, index=True)
    password = db.Column(db.String(64), nullable=False)
    user_role_id = db.Column(db.Integer, db.ForeignKey("user_role.user_role_id"))
    status = db.Column(db.Enum(UserStatus), nullable=False)

    # relationships
    instructors = db.relationship('Instructor', backref='user_details', cascade=CASCADE)
    emergency_contact = db.relationship('UserEmergencyContact', backref='user', cascade=CASCADE)

    def __init__(self, user_id, first_name, status):
        self.user_id = user_id
        self.first_name = first_name
        self.status = status

    def __repr__(self):
        return '<User %r %r %r>' % self.user_id, self.first_name, self.status


class UserEmergencyContact(db.Model):
    __tablename__ = "user_emergency_contact"
    contact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    contact_person = db.Column(db.String(120), nullable=True)
    relationship = db.Column(db.String(40), nullable=True)
    contact_no = db.Column(db.String(40), nullable=True, index=True)

    def __init__(self, contact_id, contact_person, relationship):
        self.contact_id = contact_id
        self.contact_person = contact_person
        self.relationship = relationship

    def __repr__(self):
        return '<UserEmergencyContact %r %r %r>' % self.contact_id, self.contact_id, self.contact_id
