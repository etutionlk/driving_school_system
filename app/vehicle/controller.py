"""
Name : controller.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 09/07/2023 7:49 PM
Desc: controller.py
"""
import traceback
from http import HTTPStatus

from flask import request, make_response, jsonify
from flask_restx import Resource

from app.util.dto import VehicleDTO, VehicleUpdateDTO
from app.vehicle.schema import vehicle, vehicle_model, vehicle_success_response, vehicle_error_response, \
    vehicle_manufacturer_response_model, vehicle_update_model
from app.vehicle.service import VehicleService


@vehicle.route("/vehicle/<int:vehicle_id>")
class Vehicle(Resource):

    @vehicle.response(HTTPStatus.CREATED, 'Created', vehicle_success_response, validate=True)
    @vehicle.response(HTTPStatus.BAD_REQUEST, 'Bad Request', vehicle_error_response)
    def get(self, vehicle_id: int):
        """Get a vehicle details"""
        try:
            results = VehicleService.get_data_by_id(record_id=vehicle_id, is_manufacturer=False)
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)

    @vehicle.response(HTTPStatus.CREATED, 'Created', vehicle_success_response, validate=True)
    @vehicle.response(HTTPStatus.BAD_REQUEST, 'Bad Request', vehicle_error_response)
    @vehicle.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Server Error', vehicle_error_response)
    @vehicle.expect(vehicle_update_model, validate=True)
    def put(self, vehicle_id: int):
        """Update vehicle details"""
        try:
            request_data = request.get_json()
            vehicle_dto = VehicleUpdateDTO(**request_data)
            filtered_date = {k: v for k, v in vehicle_dto.model_dump().items() if v is not None}
            VehicleService.update_vehicle(vehicle_id=vehicle_id, data=filtered_date)
            return make_response(jsonify({"message": "Vehicle updated successfully.",
                                          "is_error": False}), HTTPStatus.CREATED)
        except Exception as e:
            print(traceback.format_exc())
            return make_response(jsonify({"message": str(e), "is_error": True}), HTTPStatus.INTERNAL_SERVER_ERROR)

    def delete(self, vehicle_id: int):
        """Delete a vehicle"""
        try:
            VehicleService.delete_candidate(vehicle_id=vehicle_id)

            return make_response(jsonify({"message": "Vehicle deleted successfully.",
                                          "is_error": False}), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)

    @vehicle.response(HTTPStatus.BAD_REQUEST, 'Bad Request', vehicle_error_response)
    @vehicle.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Server Error', vehicle_error_response)
    @vehicle.response(HTTPStatus.CREATED, 'OK', vehicle_success_response, validate=True)
    @vehicle.param("status", "Vehicle Status", required=True)
    def patch(self, vehicle_id: int):
        """Change the status of a vehicle"""
        try:
            status = request.args.get('status', type=str)
            VehicleService.update_vehicle(vehicle_id=vehicle_id, data={"status": status.upper()})
            return make_response(jsonify({"message": "Vehicle status updated successfully.",
                                          "is_error": False}), HTTPStatus.CREATED)
        except Exception as e:
            print(traceback.format_exc())
            return make_response(jsonify({"message": str(e), "is_error": True}), HTTPStatus.INTERNAL_SERVER_ERROR)


@vehicle.route("/vehicle")
class VehicleCreate(Resource):

    @vehicle.response(HTTPStatus.CREATED, 'Created', vehicle_success_response, validate=True)
    @vehicle.response(HTTPStatus.BAD_REQUEST, 'Bad Request', vehicle_error_response)
    @vehicle.expect(vehicle_model, validate=True)
    def post(self):
        """Add a vehicle to the driving school"""
        try:
            request_data = request.get_json()
            vehicle_dto = VehicleDTO(**request_data)
            print(vehicle_dto)

            VehicleService.save_vehicle(vehicle=vehicle_dto)
            return make_response(jsonify({"message": "Vehicle is added successfully.",
                                          "is_error": False}), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)


@vehicle.route("/vehicle/all")
class VehicleAll(Resource):

    @vehicle.param("offset", "Offset")
    @vehicle.param("limit", "Limit")
    @vehicle.param("status", "Vehicle Status")
    def get(self):
        """Get all registered vehicles"""
        try:
            offset = request.args.get('offset', type=int)
            limit = request.args.get('limit', type=int)
            status = request.args.get('status', type=str)

            results = VehicleService.get_all_data(offset=offset if offset else None, limit=limit if limit else None,
                                                  status=status if status else None, only_manufacturers=False)
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)


@vehicle.route("/vehicles_by_status")
class VehicleAllByStatus(Resource):

    @vehicle.param("status", "Vehicle Status")
    def get(self):
        """Get all registered vehicles by vehicle status"""
        try:
            status = request.args.get('status', type=str)

            results = VehicleService.get_all_data(status=status if status else None, only_manufacturers=False)
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)


@vehicle.route("/vehicle_manufacturers")
class VehicleManufacturers(Resource):

    @vehicle.param("offset", "Offset")
    @vehicle.param("limit", "Limit")
    @vehicle.response(HTTPStatus.CREATED, 'Created', [vehicle_manufacturer_response_model], validate=True)
    @vehicle.response(HTTPStatus.BAD_REQUEST, 'Bad Request', vehicle_error_response)
    def get(self):
        """Get all vehicle manufacturers"""
        try:
            offset = request.args.get('offset', type=int)
            limit = request.args.get('limit', type=int)

            results = VehicleService.get_all_data(offset=offset if offset else None, limit=limit if limit else None)
            return make_response(jsonify(results), HTTPStatus.CREATED)
        except Exception as e:
            return make_response(jsonify({"is_error": True, "message": str(e)}), HTTPStatus.BAD_REQUEST)
