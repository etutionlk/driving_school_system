"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/06/2023 7:13 AM
Desc: models.py
"""
from app.extensions import db
from app.util import Status
from app.util.constants import CASCADE


class LicenseClass(db.Model):
    __tablename__ = "license_class"
    license_class_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    license_class = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    other_eligible_classes = db.Column(db.String(150), nullable=True)

    # relationships
    license_category = db.relationship('LicenseCategory', backref='license_class', cascade=CASCADE)

    def __init__(self, license_class, description, other_eligible_classes=None):
        self.license_class = license_class
        self.description = description
        self.other_eligible_classes = other_eligible_classes

    def __repr__(self):
        return '<LicenseClass %r %r>' % self.license_class, self.description


class LicenseCategory(db.Model):
    __tablename__ = "license_category"
    license_category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    license_class_id = db.Column(db.Integer, db.ForeignKey("license_class.license_class_id"))
    description = db.Column(db.Text, nullable=True)
    skilled_category_fee = db.Column(db.Float, nullable=False)
    unskilled_category_fee = db.Column(db.Float, nullable=False)
    skilled_no_of_lessons = db.Column(db.Integer, nullable=False, default=0)
    unskilled_no_of_lessons = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)

    # relationships
    candidates = db.relationship('CandidateLicenseCategory', backref='license_category', cascade=CASCADE)

    def __repr__(self):
        return '<LicenseCategory %r %r>' % self.license_category_id, self.license_category


class CandidateLicenseCategory(db.Model):
    __tablename__ = "candidate_license_category"
    candidate_license_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    license_category_id = db.Column(db.Integer, db.ForeignKey("license_category.license_category_id"))
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.candidate_id"))
    is_skilled = db.Column(db.Boolean, nullable=False)

    def __init__(self, candidate_license_id, candidate_id):
        self.candidate_license_id = candidate_license_id
        self.candidate_id = candidate_id

    def __repr__(self):
        return '<CandidateLicenseCategory %r %r>' % self.candidate_license_id, self.candidate_id
