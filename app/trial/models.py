"""
Name : candidate_ids.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/06/2023 7:26 AM
Desc: candidate_ids.py
"""
from app.extensions import db
from app.util import ExamStatus


class Trial(db.Model):
    __tablename__ = "trial"
    trial_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.candidate_id"))
    trial_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum(ExamStatus), nullable=False)

    def __init__(self, trial_id, candidate_id, status):
        self.trial_id = trial_id
        self.candidate_id = candidate_id
        self.status = status

    def __repr__(self):
        return '<Trial %r %r %r>' % self.trial_id, self.candidate_id, self.status
