"""
Name : service
Author : Chinthaka Maduranga
Contact : chinthaka.maduranga@blackswan-technologies.com
Time : 27/06/2023 12:53 PM
Desc: service
"""
from app.candidate.models import User
from app.extensions import db

db_session = db.session


class CandidateService:

    @staticmethod
    def get_user(id: str):
        data = db_session.query(User).filter(User.id == id).all()
        return data
