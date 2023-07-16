"""
Name : service.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 11/07/2023 7:13 AM
Desc: service.py
"""
import traceback

from sqlalchemy.exc import DatabaseError, NoResultFound

from app.util import VehicleStatus
from app.util.dto import VehicleDTO
from app.util.exceptions import NoResultFoundException, DataIsEmptyException
from app.vehicle.models import VehicleManufacturer, Vehicle
from app.extensions import db

# database session
db_session = db.session


class VehicleService:
    @staticmethod
    def get_all_data(offset: int = None, limit: int = None, only_manufacturers: bool = True, status: str = None) \
            -> list:
        all_results = []
        try:
            if only_manufacturers:
                results = db_session.query(VehicleManufacturer)
            else:
                results = db_session.query(Vehicle)

            if status:
                results = results.filter(Vehicle.status == status)

            if offset:
                results = results.offset(offset)
            if limit:
                results = results.limit(limit)

            results.all()
            for result in results:

                if only_manufacturers:
                    all_results.append({"manufacturer_id": result.manufacturer_id, "manufacturer": result.manufacturer})
                else:
                    all_results.append({"vehicle_id": result.vehicle_id, "model": result.model,
                                        "registration_no": result.registration_no,
                                        "manufacturer": result.manufacturer.manufacturer,
                                        "status": result.status.value})

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return all_results

    @staticmethod
    def get_data_by_id(record_id: int, is_manufacturer: bool = False) -> dict:
        result = {}
        try:
            if is_manufacturer:
                results = db_session.query(VehicleManufacturer). \
                    filter(VehicleManufacturer.manufacturer_id == record_id).first()
                result = {"manufacturer_id": results.manufacturer_id,
                          "manufacturer": results.manufacturer} if results else {}

            else:
                results = db_session.query(Vehicle).filter(Vehicle.vehicle_id == record_id).first()
                result = {"vehicle_id": results.vehicle_id, "model": results.model,
                          "registration_no": results.registration_no,
                          "manufacturer": results.manufacturer.manufacturer,
                          "status": results.status.value} if results else {}

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound:
            print(traceback.format_exc())

        return result

    @staticmethod
    def save_vehicle(vehicle: VehicleDTO) -> bool:
        try:
            has_manufacturer = VehicleService.get_data_by_id(record_id=vehicle.manufacturer_id, is_manufacturer=True)

            if len(has_manufacturer) == 0:
                raise ValueError("Invalid Manufacturer ID.")

            db_session.add(Vehicle(model=vehicle.model, registration_no=vehicle.registration_no,
                                   manufacturer_id=vehicle.manufacturer_id, status=VehicleStatus.WORKING))

            db_session.commit()

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return True

    @staticmethod
    def update_vehicle(vehicle_id: int, data: dict) -> bool:
        try:
            # check vehicle is exists
            has_vehicle = VehicleService.get_data_by_id(record_id=vehicle_id)

            if len(has_vehicle) == 0:
                raise NoResultFoundException(message="No Vehicle Found.")

            if "manufacturer_id" in data:
                has_manufacturer = VehicleService.get_data_by_id(record_id=data["manufacturer_id"],
                                                                 is_manufacturer=True)

                if len(has_manufacturer) == 0:
                    raise ValueError("Invalid Manufacturer ID.")

            if "status" in data and  not VehicleStatus.has_value(data["status"]):
                raise ValueError("Invalid Vehicle Status.")

            if len(data) == 0:
                raise DataIsEmptyException(message="Update data is empty.")

            db_session.query(Vehicle).filter(Vehicle.vehicle_id == vehicle_id).update(data)
            db_session.commit()
        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except Exception as e:
            print(traceback.format_exc())
            raise e

        return True

    @staticmethod
    def delete_vehicle(vehicle_id: int) -> bool:
        try:
            record = db_session.query(Vehicle).filter(Vehicle.vehicle_id == vehicle_id).one()
            db_session.delete(record)
            db_session.commit()
        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())
            raise NoResultFoundException(message="Vehicle is not found.")

        return True
