"""
Name : controller.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 20/06/2023 8:21 AM
Desc: controller.py
"""
from flask_restx import Resource
from app.candidate.schema import candidate, candidate_model
from app.candidate.service import CandidateService


@candidate.route("/<int:id>")
class Candidate(Resource):
    def get(self, id):
        user = CandidateService.get_user(id=id)
        return {'task': 'Say Hello, {}!'.format(user[0].username)}, 201

    @candidate.expect(candidate_model)
    def post(self):
        return {"message": "candidate added successfully."}
