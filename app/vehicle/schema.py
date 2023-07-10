"""
Name : schema.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 09/07/2023 7:51 PM
Desc: schema.py
"""
from flask_restx import Namespace, fields

vehicle = Namespace('Vehicle', description='Driving school vehicles')

vehicle_model = vehicle.model("Vehicle", {
    "model": fields.String,
    "registration_no": fields.String,
    "manufacturer_id": fields.Integer
})

vehicle_error_response = vehicle.model("ErrorResponse", {
    "is_error": fields.Boolean(default=True),
    "message": fields.String(default="Bad Request")
})

vehicle_success_response = vehicle.model("SuccessResponse", {
    "message": fields.String(default="Success")
})
