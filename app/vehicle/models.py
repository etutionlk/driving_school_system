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
    manufacturer = db.Column(db.String(50), nullable=False)

    def __init__(self, manufacturer_id, manufacturer):
        self.manufacturer_id = manufacturer_id
        self.manufacturer = manufacturer

    def __repr__(self):
        return '<VehicleManufacturer %r %r>' % self.manufacturer_id, self.manufacturer


class Vehicle(db.Model):
    __tablename__ = "vehicle"
    vehicle_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(50), nullable=False)
    registration_no = db.Column(db.String(50), unique=True, nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey("vehicle_manufacturer.manufacturer_id"))
    status =  db.Column(db.Enum(VehicleStatus), nullable=False)

    # relationships
    lesson_schedules = db.relationship('LessonSchedule', backref='instructor', cascade=CASCADE)
    manufacturer = db.relationship('VehicleManufacturer', backref='vehicle', cascade=CASCADE)

    def __init__(self, vehicle_id, model):
        self.vehicle_id = vehicle_id
        self.model = model

    def __repr__(self):
        return '<Vehicle %r %r>' % self.vehicle_id, self.model
    
    
    