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

candidate_response_model = candidate.model("CandidateResponse", {
    "candidate_id": fields.Integer(default=1),
    "fullname": fields.String(default="Tom Cruise"),
    "date_of_birth": fields.String(default="1987-06-01"),
    "mobile_no_1": fields.String(default="0771234123"),
    "mobile_no_2": fields.String(default=""),
    "nic_no": fields.String(default="222222222V"),
    "address": fields.String(default="No: 22/A, Park Rd, Colombo"),
    "sex": fields.String(default="Male"),
    "schedule": fields.List(fields.String(), default=[{"lesson_date": "2023-01-02", "lesson_time": "12:30:00",
                                                      "instructor_name": "Anura Jayantha", "car_model": "Alto",
                                                      "registration_no": "CS-1234"}])
})
