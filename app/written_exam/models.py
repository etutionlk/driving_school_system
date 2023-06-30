"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/06/2023 7:36 AM
Desc: models.py
"""
from app.extensions import db
from app.util import ExamStatus


class WrittenExam(db.Model):
    __tablename__ = "written_exam"
    exam_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.candidate_id"))
    exam_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum(ExamStatus), nullable=False)

    def __init__(self, exam_id, candidate_id, status):
        self.exam_id = exam_id
        self.candidate_id = candidate_id
        self.status = status

    def __repr__(self):
        return '<WrittenExam %r %r %r>' % self.exam_id, self.candidate_id, self.status
