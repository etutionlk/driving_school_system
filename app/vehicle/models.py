"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/06/2023 7:14 AM
Desc: models.py
"""
from app.extensions import db
from app.util import VehicleStatus
from app.util.constants import CASCADE


class VehicleManufacturer(db.Model):
    __tablename__ = "vehicle_manufacturer"
    manufacturer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    manufacturer = db.Column(db.String(50), nullable=False, unique=True)

    # relationship
    vehicles = db.relationship('Vehicle', backref='manufacturer', cascade=CASCADE)

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def __repr__(self):
        return '<VehicleManufacturer %r>' % self.manufacturer


class Vehicle(db.Model):
    __tablename__ = "vehicle"
    vehicle_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(50), nullable=False)
    registration_no = db.Column(db.String(50), unique=True, nullable=False, index=True)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey("vehicle_manufacturer.manufacturer_id"))
    status = db.Column(db.Enum(VehicleStatus), nullable=False)

    # relationships
    lesson_schedules = db.relationship('LessonSchedule', backref='vehicle', cascade=CASCADE)

    def __init__(self, model="", registration_no="", manufacturer_id=0, status=None):
        self.model = model
        self.registration_no = registration_no
        self.manufacturer_id = manufacturer_id
        self.status = status


    def __repr__(self):
        return '<Vehicle %r %r>' % self.vehicle_id, self.model
