"""
Name : models.py
Author : Chinthaka Maduranga
Contact : chinthaka.maduranga@blackswan-technologies.com
Time : 09/04/2023 6:48 PM
Desc: models
"""
from app.extensions import db
from app.util import Sex, CandidateStatus, Title
from app.util.constants import CASCADE


class Candidate(db.Model):
    __tablename__ = "candidate"
    candidate_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Enum(Title), nullable=False, comment="Ex: Mr., Mrs., Ms., Rev., ")
    fullname = db.Column(db.String(120), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    mobile_no_1 = db.Column(db.String(40), nullable=False)
    mobile_no_2 = db.Column(db.String(40), nullable=True, comment="This number is used to contact candidate, "
                                                                  "if his/her mobile number is on not responding.")
    nic_no = db.Column(db.String(40), unique=True, nullable=False, comment="National Identity Card No.", index=True)
    address = db.Column(db.Text, nullable=True)
    sex = db.Column(db.Enum(Sex), nullable=False)
    has_vehicle_license = db.Column(db.Boolean, nullable=False,
                                    comment='if already have license true otherwise false')
    registered_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(CandidateStatus), nullable=False)

    # relationships
    license_categories = db.relationship('CandidateLicenseCategory', backref='candidate', cascade=CASCADE)
    written_exams = db.relationship('WrittenExam', backref='candidate', cascade=CASCADE)
    lesson_schedules = db.relationship('LessonSchedule', backref='candidate', cascade=CASCADE)
    payments = db.relationship('CandidatePayment', backref='candidate', cascade=CASCADE)
    trials = db.relationship('Trial', backref='candidate', cascade=CASCADE)

