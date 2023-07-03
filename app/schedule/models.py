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
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.candidate_id"))
    licence_category_id = db.Column(db.Integer, db.ForeignKey("licence_category.licence_category_id"))
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructor.instructor_id"))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.vehicle_id"))
    lesson_date = db.Column(db.Date, nullable=False)
    lesson_time = db.Column(db.Time, nullable=False)
    lesson_status = db.Column(db.Enum(LessonStatus), nullable=False)
