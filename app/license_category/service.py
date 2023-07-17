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
from app.util.dto import LicenseCategoryDTO
from app.util.exceptions import NoResultFoundException

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

    @staticmethod
    def get_license_class_by_class(license_class: str):
        results = {}
        try:
            result = db_session.query(LicenseClass).filter(LicenseClass.license_class == license_class).one()
            results = {"license_class_id": result.license_class_id,
                       "license_class": result.license_class,
                       "description": result.description,
                       "other_eligible_classes": result.other_eligible_classes.split(",")}

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return results

    @staticmethod
    def get_license_class_by_class_id(license_class_id: int):
        results = {}
        try:
            result = db_session.query(LicenseClass).filter(LicenseClass.license_class_id == license_class_id).one()
            results = {"license_class_id": result.license_class_id,
                       "license_class": result.license_class,
                       "description": result.description,
                       "other_eligible_classes": result.other_eligible_classes.split(",")}

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return results

    @staticmethod
    def get_license_category_by_id(license_category_id: int):
        results = {}
        try:
            result = db_session.query(LicenseCategory).filter(LicenseCategory.license_category_id ==
                                                              license_category_id).one()

            results = {"license_category_id": result.license_category_id,
                       "license_class": result.license_class.license_class,
                       "licence_description": result.license_class.description,
                       "other_eligible_classes": result.license_class.other_eligible_classes,
                       "description": result.description,
                       "skilled_category_fee": result.skilled_category_fee,
                       "unskilled_category_fee": result.unskilled_category_fee,
                       "skilled_no_of_lessons": result.skilled_no_of_lessons,
                       "unskilled_no_of_lessons": result.unskilled_no_of_lessons,
                       "status": result.status.value}

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return results

    @staticmethod
    def get_license_category_by_license_class_id(license_class_id: int):
        results = {}
        try:
            result = db_session.query(LicenseCategory).filter(LicenseCategory.license_class_id ==
                                                              license_class_id).one()

            results = {"license_category_id": result.license_category_id,
                       "license_class": result.license_class.license_class,
                       "licence_description": result.license_class.description,
                       "other_eligible_classes": result.license_class.other_eligible_classes,
                       "description": result.description,
                       "skilled_category_fee": result.skilled_category_fee,
                       "unskilled_category_fee": result.unskilled_category_fee,
                       "skilled_no_of_lessons": result.skilled_no_of_lessons,
                       "unskilled_no_of_lessons": result.unskilled_no_of_lessons,
                       "status": result.status.value}

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return results

    @staticmethod
    def get_all_license_categories(offset: int = None, limit: int = None, status: str = None) \
            -> list:
        all_results = []
        try:
            results = db_session.query(LicenseCategory)

            if status:
                results = results.filter(LicenseCategory.status == status)

            if offset:
                results = results.offset(offset)
            if limit:
                results = results.limit(limit)

            results.all()
            for result in results:
                all_results.append({"license_category_id": result.license_category_id,
                                    "license_class": result.license_class.license_class,
                                    "licence_description": result.license_class.description,
                                    "other_eligible_classes": result.license_class.other_eligible_classes,
                                    "description": result.description,
                                    "skilled_category_fee": result.skilled_category_fee,
                                    "unskilled_category_fee": result.unskilled_category_fee,
                                    "skilled_no_of_lessons": result.skilled_no_of_lessons,
                                    "unskilled_no_of_lessons": result.unskilled_no_of_lessons,
                                    "status": result.status.value})

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return all_results


    @staticmethod
    def save_license_category(license_category: LicenseCategoryDTO):
        try:
            is_valid_license_class = LicenseService.get_license_class_by_class_id(
                license_class_id=license_category.license_class_id)

            if len(is_valid_license_class) == 0:
                raise ValueError("License Class ID is NOT valid.")

            has_license_category = LicenseService.get_license_category_by_license_class_id(
                license_class_id=license_category.license_class_id)

            if len(has_license_category) > 0:
                raise ValueError("License Category is already registered for License Class ID: {}".format(
                    license_category.license_class_id))

            values = license_category.model_dump()
            db_session.add(LicenseCategory(**values))

            db_session.commit()

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return True

    @staticmethod
    def delete_license_category(license_category_id: int) -> bool:
        try:
            has_license_category = LicenseService.get_license_category_by_id(license_category_id=license_category_id)

            if len(has_license_category) == 0:
                raise ValueError("Invalid License Category ID")

            record = db_session.query(LicenseCategory).filter(LicenseCategory.license_category_id ==
                                                              license_category_id).one()
            db_session.delete(record)
            db_session.commit()
        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())
            raise NoResultFoundException(message="License Category is not found.")

        return True
