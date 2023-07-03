"""
Name : schema.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 21/06/2023 9:55 PM
Desc: schema.py
"""
from flask_restx import Namespace, fields

candidate = Namespace('Candidate', description='Candidate related operations')

candidate_model = candidate.model("Candidate", {
    "title": fields.String,
    "fullname": fields.String,
    "date_of_birth": fields.String(required=True),
    "mobile_no_1": fields.String(required=True),
    "mobile_no_2": fields.String,
    "nic_no": fields.String(required=True),
    "address": fields.String,
    "sex": fields.String(required=True),
    "has_vehicle_licence": fields.Boolean(required=True)
})
