"""
Name : controller.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 20/06/2023 8:21 AM
Desc: controller.py
"""
from flask_restx import Resource
from app.candidate.schema import candidate, candidate_model


@candidate.route("/<int:id>")
class Candidate(Resource):
    def get(self, id):
        return {'task': 'Say Hello, World!'}, 201

    @candidate.expect(candidate_model)
    def post(self):
        return {"message": "candidate added successfully."}
