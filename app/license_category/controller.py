"""
Name : controller.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 13/07/2023 6:18 AM
Desc: controller.py
"""
from http import HTTPStatus

from flask import make_response, jsonify
from flask_restx import Resource

from app.license_category.schema import license_category, license_response_model, license_error_response
from app.license_category.service import LicenseService


@license_category.route("/license/all_approved_license_classes")
class LicenseClass(Resource):

    @license_category.response(HTTPStatus.CREATED, 'Created', [license_response_model], validate=True)
    @license_category.response(HTTPStatus.BAD_REQUEST, 'Bad Request', license_error_response)
    def get(self):
        """All government approved license classes"""
        try:
            results = LicenseService.get_all_license_classes()
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)
