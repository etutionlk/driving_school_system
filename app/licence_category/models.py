"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/06/2023 7:13 AM
Desc: models.py
"""
from app.extensions import db
from app.util import Status


class LicenceCategory(db.Model):
    __tablename__ = "licence_category"
    licence_category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    licence_category = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    skilled_category_fee = db.Column(db.Float, nullable=False)
    unskilled_category_fee = db.Column(db.Float, nullable=False)
    skilled_no_of_lessons = db.Column(db.Integer, nullable=False)
    unskilled_no_of_lessons = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)

    def __init__(self, licence_category_id, licence_category):
        self.licence_category_id = licence_category_id
        self.licence_category = licence_category

    def __repr__(self):
        return '<LicenceCategory %r %r>' % self.licence_category_id, self.licence_category


class CandidateLicenceCategory(db.Model):
    __tablename__ = "candidate_licence_category"
    candidate_licence_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    licence_category_id = db.Column(db.Integer, db.ForeignKey("licence_category.licence_category_id"))
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.candidate_id"))
    is_skilled = db.Column(db.Boolean, nullable=False)

    def __init__(self, candidate_licence_id, candidate_id):
        self.candidate_licence_id = candidate_licence_id
        self.candidate_id = candidate_id

    def __repr__(self):
        return '<CandidateLicenceCategory %r %r>' % self.candidate_licence_id, self.candidate_id
