"""
Name : schema.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 21/06/2023 9:55 PM
Desc: schema.py
"""
from flask_restx import Namespace, fields

candidate = Namespace('Candidate', description='Candidate related operations')

candidate_model = candidate.model("Course", {
    "id": fields.Integer,
    "name": fields.String
})