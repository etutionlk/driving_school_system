"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 29/06/2023 10:54 PM
Desc: models.py
"""
from app.extensions import db
from app.util import LessonStatus


class LessonSchedule(db.Model):
    __tablename__ = "lesson_schedule"
    lesson_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.candidate_id", onupdate="CASCADE", ondelete="CASCADE"))
    licence_category_id = db.Column(db.Integer, db.ForeignKey("licence_category.licence_category_id"))
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructor.instructor_id"))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.vehicle_id"))
    lesson_date = db.Column(db.Datetime, nullable=False)
    lesson_status = db.Column(db.Enum(LessonStatus), nullable=False)

    def __init__(self, lesson_id, candidate_id, lesson_status):
        self.lesson_id = lesson_id
        self.candidate_id = candidate_id
        self.lesson_status = lesson_status

    def __repr__(self):
        return '<LessonSchedule %r %r %r>' % self.lesson_id, self.candidate_id, self.lesson_status
