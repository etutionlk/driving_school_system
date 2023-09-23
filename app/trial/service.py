"""
Name : service.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 23/07/2023 6:44 PM
Desc: service.py
"""
import traceback

from sqlalchemy.exc import DatabaseError, NoResultFound

from app import Trial
from app.candidate.service import CandidateService
from app.extensions import db
from app.util.dto import TrialDTO

db_session = db.session


class TrialService:

    @staticmethod
    def save_trial(candidate_id: int, candidate_trial: TrialDTO):
        try:
            # check candidate is exists
            has_candidate = CandidateService.get_candidate_by_candidate_id(candidate_id=candidate_id)

            if len(has_candidate) == 0:
                raise ValueError("Candidate is NOT exists.")

            values = candidate_trial.model_dump()
            db_session.add(Trial(**values))

            db_session.commit()

        except DatabaseError as e:
            print(traceback.format_exc())
            raise e
        except NoResultFound as e:
            print(traceback.format_exc())

        return True
