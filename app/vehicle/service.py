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
from app.vehicle.models import VehicleManufacturer, Vehicle
from app.extensions import db

# database session
db_session = db.session


class VehicleService:
    @staticmethod
    def get_all_data(offset: int = None, limit: int = None, only_manufacturers: bool = True, status: str = None):
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
    def get_data_by_id(record_id: int, is_manufacturer: bool = False):
        result = {}
        try:
            if is_manufacturer:
                results = db_session.query(VehicleManufacturer). \
                    filter(VehicleManufacturer.manufacturer_id == record_id).first()
                result = {"manufacturer_id": results.manufacturer_id, "manufacturer": results.manufacturer}


            else:
                results = db_session.query(Vehicle).filter(Vehicle.vehicle_id == record_id).first()
                result = {"vehicle_id": results.vehicle_id, "model": results.model,
                          "registration_no": results.registration_no,
                          "manufacturer": results.manufacturer.manufacturer, "status": results.status.value}

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return result
