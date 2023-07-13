"""
Name : service.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 13/07/2023 7:30 AM
Desc: service.py
"""
import traceback

from sqlalchemy.exc import DatabaseError, NoResultFound

from app.license_category.models import LicenseClass, LicenseCategory, CandidateLicenseCategory
from app.extensions import db

db_session = db.session


class LicenseService:

    @staticmethod
    def get_all_license_classes(offset: int = 0, limit: int = 20):
        all_results = []
        try:
            results = db_session.query(LicenseClass).filter().offset(offset).limit(limit).all()
            for result in results:
                all_results.append({
                    "license_class_id": result.license_class_id,
                    "license_class": result.license_class,
                    "description": result.description,
                    "other_eligible_classes": result.other_eligible_classes.split(",")
                })

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return all_results
