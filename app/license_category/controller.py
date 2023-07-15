"""
Name : controller.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 13/07/2023 6:18 AM
Desc: controller.py
"""
from http import HTTPStatus

from flask import make_response, jsonify, request
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


@license_category.route("/license/license_class")
class SingleLicenseClass(Resource):

    @license_category.response(HTTPStatus.CREATED, 'Created', license_response_model, validate=True)
    @license_category.response(HTTPStatus.BAD_REQUEST, 'Bad Request', license_error_response)
    @license_category.param("license_class", "License Class", required=True)
    def get(self):
        """Get a single license classes"""
        try:
            license_class = request.args.get('license_class', type=str)
            results = LicenseService.get_single_license_class(license_class=license_class.upper())
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)


@license_category.route("/license/license_category/<int:license_category_id>")
class LicenseCategory(Resource):

    def get(self, license_category_id: int):
        """Get a single License Category"""
        pass

    def put(self, license_category_id: int):
        """Update a single License Category"""
        pass

    def delete(self, license_category_id: int):
        """Delete a Licene Category"""
        pass


@license_category.route("/license/license_category")
class LicenseCategoryPost(Resource):

    def post(self):
        """Create a License Category"""
        pass


@license_category.route("/license/all_license_categories")
class AllLicenseCategories(Resource):
    def get(self):
        """Get All License Categories"""
        pass
