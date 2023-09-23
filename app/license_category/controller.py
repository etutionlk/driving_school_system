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

from app.license_category.schema import license_category, license_response_model, license_error_response, \
    license_category_response_model, license_category_error_response, license_category_model, \
    license_category_success_response, license_update_category_model
from app.license_category.service import LicenseService
from app.util.dto import LicenseCategoryDTO


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
            results = LicenseService.get_license_class_by_class(license_class=license_class.upper())
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)


@license_category.route("/license/license_category/<int:license_category_id>")
class LicenseCategory(Resource):

    @license_category.response(HTTPStatus.CREATED, 'Created', license_category_response_model, validate=True)
    @license_category.response(HTTPStatus.BAD_REQUEST, 'Bad Request', license_category_error_response)
    def get(self, license_category_id: int):
        """Get a single License Category"""
        try:
            results = LicenseService.get_license_category_by_id(license_category_id=license_category_id)
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)

    @license_category.expect(license_update_category_model, validate=True)
    @license_category.response(HTTPStatus.CREATED, 'Created', license_category_success_response, validate=True)
    @license_category.response(HTTPStatus.BAD_REQUEST, 'Bad Request', license_category_error_response)
    def put(self, license_category_id: int):
        """Update a single License Category"""
        pass

    def delete(self, license_category_id: int):
        """Delete a License Category"""
        try:
            LicenseService.delete_license_category(license_category_id=license_category_id)

            return make_response(jsonify({"message": "Vehicle deleted successfully.",
                                          "is_error": False}), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)


@license_category.route("/license/license_category")
class LicenseCategoryPost(Resource):

    @license_category.expect(license_category_model, validate=True)
    @license_category.response(HTTPStatus.CREATED, 'Created', license_category_success_response, validate=True)
    @license_category.response(HTTPStatus.BAD_REQUEST, 'Bad Request', license_category_error_response)
    def post(self):
        """Create a License Category"""
        try:
            request_data = request.get_json()
            license_cat = LicenseCategoryDTO(**request_data)

            LicenseService.save_license_category(license_category=license_cat)
            return make_response(jsonify({"message": "License Category is added successfully.",
                                          "is_error": False}), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)


@license_category.route("/license/all_license_categories")
class AllLicenseCategories(Resource):

    @license_category.param("offset", "Offset")
    @license_category.param("limit", "Limit")
    @license_category.param("status", "License Category Status")
    @license_category.response(HTTPStatus.CREATED, 'Created', [license_category_response_model], validate=True)
    def get(self):
        """Get All License Categories"""
        try:
            offset = request.args.get('offset', type=int)
            limit = request.args.get('limit', type=int)
            status = request.args.get('status', type=str)

            results = LicenseService.get_all_license_categories(offset=offset if offset else None,
                                                                limit=limit if limit else None,
                                                                status=status if status else None)
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)
