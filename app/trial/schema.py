"""
Name : schema.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 23/07/2023 6:44 PM
Desc: schema.py
"""
from flask_restx import Namespace, fields

trial = Namespace('Trial', description='Candidate Trial Operations')

trial_request_model = trial.model("TrialRequestResponse", {
    "candidate_id": fields.Integer(),
    "trial_date": fields.Date
})

trial_response_model = trial.model("TrialRequestResponse", {
    "candidate_id": fields.Integer(default=1),
    "trial_date": fields.Date(default="2023-07-24"),
    "status": fields.String(default="PASSED")
})

trial_error_response = license_error_response = trial.model("ErrorResponse", {
    "message": fields.String(default="Bad Request"),
    "is_error": fields.Boolean(default=True),
})

trial_success_response = license_success_response = trial.model("SuccessResponse", {
    "message": fields.String(default="Success"),
    "is_error": fields.Boolean(default=False)
})