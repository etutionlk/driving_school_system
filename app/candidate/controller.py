"""
Name : controller.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 20/06/2023 8:21 AM
Desc: controller.py
"""
from datetime import datetime
from http import HTTPStatus

from flask import jsonify, make_response, request
from flask_restx import Resource
from app.candidate.schema import candidate, candidate_model, candidate_response_model, candidate_error_response
from app.candidate.service import CandidateService
from app.util import Sex, CandidateStatus
from app.util.dto import CandidateDTO


@candidate.route("/candidate/<int:candidate_id>")
class Candidate(Resource):
    @candidate.param("required_schedule", validate=True, description="Load Schedule")
    @candidate.response(HTTPStatus.CREATED, 'Created', candidate_response_model, validate=True)
    @candidate.response(HTTPStatus.BAD_REQUEST, 'Bad Request', candidate_error_response)
    def get(self, candidate_id: int):
        """Get Candidate by candidate ID"""
        try:
            required_schedule = request.args.get('required_schedule', default=False, type=bool)
            result = CandidateService.get_candidate_by_candidate_id(candidate_id=candidate_id,
                                                                    required_schedule=required_schedule)
            print(result)
            return make_response(jsonify(result), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)

    def put(self, candidate_id: str):
        """Update Candidate details"""
        return jsonify({"message": "candidate updated successfully."}), 201

    def delete(self, candidate_id: str):
        """Delete Candidate by candidate ID"""
        return jsonify({"message": "candidate deleted successfully."}), 201


@candidate.route("/candidate")
class CandidateCreate(Resource):
    @candidate.expect(candidate_model, validate=True)
    def post(self):
        """Register a new candidate"""
        try:
            request_data = request.get_json()
            candidate_dto = CandidateDTO(title=request_data["title"], fullname=request_data["fullname"],
                                         date_of_birth=request_data["date_of_birth"],
                                         mobile_no_1=request_data["mobile_no_1"], nic_no=request_data["nic_no"],
                                         mobile_no_2=request_data[
                                             "mobile_no_2"] if "mobile_no_2" in request_data else None,
                                         address=request_data["address"],
                                         sex=request_data["sex"].upper(),
                                         has_vehicle_licence=request_data["has_vehicle_licence"],
                                         registered_date=datetime.now(),
                                         status=CandidateStatus.ENABLED)
            CandidateService.save_candidate(candidate_data=candidate_dto)
            return make_response(jsonify({"message": "candidate added successfully."}), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"message": str(e), "is_error": True}),
                                 HTTPStatus.INTERNAL_SERVER_ERROR)


@candidate.route("/candidate/all")
class CandidateAll(Resource):
    @candidate.param("offset", "Offset")
    @candidate.param("limit", "Limit")
    @candidate.param("required_schedule", "Load Schedules")
    @candidate.response(HTTPStatus.CREATED, 'Created', [candidate_response_model], validate=True)
    @candidate.response(HTTPStatus.BAD_REQUEST, 'Bad Request', candidate_error_response)
    def get(self):
        """Get all candidates"""
        try:
            required_schedule = request.args.get('required_schedule', default=False, type=bool)
            offset = request.args.get('offset', default=0, type=int)
            limit = request.args.get('limit', default=20, type=int)

            results = CandidateService.get_all_candidates(need_schedule=required_schedule, offset=offset, limit=limit)
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)
