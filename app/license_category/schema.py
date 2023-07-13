"""
Name : schema.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 13/07/2023 6:18 AM
Desc: schema.py
"""
from flask_restx import Namespace, fields

license_category = Namespace('License Category', description='License Category Operations')

license_response_model = license_category.model("LicenseClassResponse", {
    "license_class_id": fields.Integer(default=1),
    "license_class": fields.String(default="A"),
    "description": fields.String(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. "),
    "other_eligible_classes": fields.List(fields.String(), default=["G1", "A1"])
})

license_error_response = license_category.model("ErrorResponse", {
    "message": fields.String(default="Bad Request"),
    "is_error": fields.Boolean(default=True),
})

license_success_response = license_category.model("SuccessResponse", {
    "message": fields.String(default="Success"),
    "is_error": fields.Boolean(default=False)
})
