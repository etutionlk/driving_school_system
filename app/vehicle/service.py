"""
Name : service.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 11/07/2023 7:13 AM
Desc: service.py
"""
import traceback

from sqlalchemy.exc import DatabaseError, NoResultFound

from app.vehicle.models import VehicleManufacturer, Vehicle
from app.extensions import db

# database session
db_session = db.session


class VehicleService:
    @staticmethod
    def get_all_data(offset:int, limit: int, only_manufacturers: bool=True):
        all_results = []
        try:
            results = None
            if only_manufacturers:
                results = db_session.query(VehicleManufacturer).filter().offset(offset).limit(limit).all()
            for result in results:
                all_results.append({
                    "manufacturer_id": result.manufacturer_id,
                    "manufacturer": result.manufacturer
                })

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return all_results

