"""
Name : service
Author : Chinthaka Maduranga
Contact : chinthaka.maduranga@blackswan-technologies.com
Time : 27/06/2023 12:53 PM
Desc: service
"""
import traceback
from datetime import datetime

from app.candidate.models import Candidate
from app.extensions import db
from app.util import CandidateStatus, Sex
from app.util.dto import CandidateDTO

session = db.session


class CandidateService:

    @staticmethod
    def get_user(id: str):
        data = session.query(Candidate).filter(Candidate.candidate_id == id).all()
        return data

    @staticmethod
    def save_user(request_data: dict):
        try:
            # print(candidate_data.model_dump_json())
            session.add(Candidate(title=request_data["title"], fullname=request_data["fullname"],
                                     date_of_birth=request_data["date_of_birth"],
                                     mobile_no_1=request_data["mobile_no_1"], nic_no=request_data["nic_no"],
                                     mobile_no_2=request_data["mobile_no_2"] if "mobile_no_2" in request_data else None,
                                     address=request_data["address"],
                                     sex=Sex.MALE if request_data["sex"].lower() == "male" else Sex.FEMALE,
                                     has_vehicle_licence=request_data["has_vehicle_licence"],
                                     registered_date=datetime.strptime(request_data["registered_date"], '%Y-%m-%d'),
                                     status=CandidateStatus.ENABLED))
            session.commit()
        except Exception:
            print(traceback.format_exc())

