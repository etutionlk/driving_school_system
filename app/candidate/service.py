"""
Name : service
Author : Chinthaka Maduranga
Contact : chinthaka.maduranga@blackswan-technologies.com
Time : 27/06/2023 12:53 PM
Desc: service
"""
import traceback
from datetime import datetime

from sqlalchemy.exc import NoResultFound, DatabaseError

from app.candidate.models import Candidate
from app.extensions import db
from app.util import CandidateStatus, Sex
from app.util.dto import CandidateDTO
from app.util.exceptions import NoResultFoundException

db_session = db.session


class CandidateService:

    @staticmethod
    def get_candidate_by_candidate_id(candidate_id: int, required_schedule: bool) -> dict:
        result = {}
        try:
            data = db_session.query(Candidate).filter(Candidate.candidate_id == candidate_id).one()

            if data:

                schedule = []
                for sc in data.lesson_schedules:
                    schedule.append({"lesson_date": str(sc.lesson_date), "lesson_time": str(sc.lesson_time),
                                     "instructor_name": " ".join([sc.instructor.user_details.first_name,
                                                                  sc.instructor.user_details.last_name]),
                                     "car_model": sc.vehicle.model, "registration_no": sc.vehicle.registration_no})

                result = {"candidate_id": data.candidate_id, "fullname": data.fullname,
                          "date_of_birth": data.date_of_birth, "mobile_no_1": data.mobile_no_1,
                          "mobile_no_2": data.mobile_no_2, "nic_no": data.nic_no,
                          "address": data.address, "sex": data.sex.value,
                          "schedule": schedule if required_schedule else []}
        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound:
            print(traceback.format_exc())

        return result

    @staticmethod
    def get_candidate_by_nic_no(nic_no: str):
        try:
            data = db_session.query(Candidate).filter(Candidate.nic_no == nic_no).one()
        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound:
            print(traceback.format_exc())
            return None

        return data.candidate_id

    @staticmethod
    def save_candidate(candidate_data: CandidateDTO) -> bool:
        try:
            candidate_id = CandidateService.get_candidate_by_nic_no(nic_no=candidate_data.nic_no)

            if candidate_id:
                raise ValueError("Candidate {} is already registered.".format(candidate_data.fullname))

            db_session.add(Candidate(title=candidate_data.title, fullname=candidate_data.fullname,
                                     date_of_birth=candidate_data.date_of_birth,
                                     mobile_no_1=candidate_data.mobile_no_1, nic_no=candidate_data.nic_no,
                                     mobile_no_2=candidate_data.mobile_no_2, address=candidate_data.address,
                                     sex=candidate_data.sex, has_vehicle_licence=candidate_data.has_vehicle_licence,
                                     registered_date=candidate_data.registered_date, status=candidate_data.status))
            db_session.commit()
        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except Exception as e:
            print(traceback.format_exc())
            raise e

        return True

    @staticmethod
    def get_all_candidates(need_schedule: bool, offset: int, limit: int) -> list:
        all_results = []
        try:
            results = db_session.query(Candidate).filter().offset(offset).limit(limit).all()
            for result in results:
                all_results.append({
                    "candidate_id": result.candidate_id,
                    "candidate_name": result.fullname,
                    "schedule": [{"date": str(schedule.lesson_date), "car": schedule.vehicle.model} for schedule in
                                 result.lesson_schedules]
                })

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return all_results


    @staticmethod
    def delete_candidate(candidate_id: int) ->bool:
        try:
            record = db_session.query(Candidate).filter(Candidate.candidate_id == candidate_id).one()
            db_session.delete(record)
            db_session.commit()
        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())
            raise NoResultFoundException(message="Candidate is not found.")

        return True

