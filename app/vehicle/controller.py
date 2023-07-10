"""
Name : controller.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 09/07/2023 7:49 PM
Desc: controller.py
"""
from http import HTTPStatus

from flask_restx import Resource
from app.vehicle.schema import vehicle, vehicle_model, vehicle_success_response, vehicle_error_response


@vehicle.route("/vehicle/<int:vehicle_id>")
class Vehicle(Resource):

    @vehicle.response(HTTPStatus.CREATED, 'Created', vehicle_success_response, validate=True)
    @vehicle.response(HTTPStatus.BAD_REQUEST, 'Bad Request', vehicle_error_response)
    @vehicle.expect(vehicle_model, validate=True)
    def get(self, vehicle_id: int):
        """Get a vehicle details"""
        pass

    def put(self, vehicle_id: int):
        """Update vehicle details"""
        pass

    def delete(self, vehicle_id: int):
        """Delete a vehicle"""
        pass

    def patch(self, vehicle_id: int):
        """Change an attribute of a vehicle"""
        pass


@vehicle.route("/vehicle")
class VehicleCreate(Resource):

    @vehicle.response(HTTPStatus.CREATED, 'Created', vehicle_success_response, validate=True)
    @vehicle.response(HTTPStatus.BAD_REQUEST, 'Bad Request', vehicle_error_response)
    @vehicle.expect(vehicle_model, validate=True)
    def post(self):
        """Add a vehicle to the driving school"""
        pass


@vehicle.route("/vehicle/all")
class VehicleAll(Resource):

    @vehicle.param("offset", "Offset")
    @vehicle.param("limit", "Limit")
    @vehicle.param("status", "Vehicle Status")
    def get(self):
        """Get all registered vehicles"""
        pass

@vehicle.route("/vehicles_by_status")
class VehicleAllByStatus(Resource):

    @vehicle.param("status", "Vehicle Status")
    def get(self):
        """Get all registered vehicles by vehicle status"""
        pass

@vehicle.route("/vehicle_manufacturers")
class VehicleManufacturers(Resource):

    def get(self):
        """Get all vehicle manufacturers"""
        pass