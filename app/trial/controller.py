"""
Name : controller.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 23/07/2023 6:44 PM
Desc: controller.py
"""
from http import HTTPStatus

from flask import request, make_response, jsonify
from flask_restx import Resource

from app.trial.schema import trial, trial_request_model, trial_success_response, trial_error_response
from app.trial.service import TrialService
from app.util.dto import TrialDTO


@trial.route("/trial/<int:candidate_id>")
class TrialClass(Resource):

    def get(self, candidate_id: int):
        """Get All trial details"""
        pass

    @trial.expect(trial_request_model, validate=True)
    @trial.response(HTTPStatus.CREATED, 'Created', trial_success_response, validate=True)
    @trial.response(HTTPStatus.BAD_REQUEST, 'Bad Request', trial_error_response)
    def post(self, candidate_id):
        """Add trial for a candidate"""
        try:
            request_data = request.get_json()
            candidate_trial = TrialDTO(candidate_id=request_data["candidate_id"], trial_date=request_data["trial_date"],
                                       status=ExamStatus)

            TrialService.save_trial(candidate_id=candidate_id, candidate_trial=candidate_trial)
            return make_response(jsonify({"message": "License Category is added successfully.",
                                          "is_error": False}), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)

    def delete(self, candidate_id: int):
        """Delete trial information of a candidate"""
        pass

    def patch(self, candidate_id):
        """Update trial information"""
        pass


@trial.route("/trial_by_status")
class TrialStatusClass(Resource):

    def get(self):
        """Get Trial dates by Status"""
        pass


@trial.route("/candidates_by_trial_date")
class TrialStatusClass(Resource):

    def get(self):
        """Get candidates by the trial date"""
        pass
