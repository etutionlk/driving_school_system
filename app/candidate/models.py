"""
Name : models.py
Author : Chinthaka Maduranga
Contact : chinthaka.maduranga@blackswan-technologies.com
Time : 09/04/2023 6:48 PM
Desc: models
"""
from app.extensions import db
from app.util import Sex, CandidateStatus


class Candidate(db.Model):
    __tablename__ = "candidate"
    candidate_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), nullable=False, comment="Ex: Mr., Mrs., Ms., Rev., ")
    fullname = db.Column(db.String(120), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    nic_no = db.Column(db.String(40), unique=True, nullable=False, comment="National Identity Card No.")
    address = db.Column(db.Text, nullable=True)
    sex = db.Column(db.Enum(Sex), nullable=False)
    has_vehicle_licence = db.Column(db.Boolean, nullable=False,
                                    comment='if already have license true otherwise false')
    registered_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(CandidateStatus), nullable=False)

    def __init__(self, candidate_id, fullname):
        self.candidate_id = candidate_id
        self.fullname = fullname

    def __repr__(self):
        return '<Candidate %r %r>' % self.candidate_id, self.fullname
