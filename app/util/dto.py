"""
Name : dto.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 02/07/2023 7:55 PM
Desc: dto.py
"""
import enum
from datetime import date
from typing import Optional

from pydantic import BaseModel, constr, field_validator

from app.util import Sex, CandidateStatus


class CandidateDTO(BaseModel):
    title: constr()
    fullname: constr()
    date_of_birth: constr()
    mobile_no_1: constr()
    mobile_no_2: Optional[constr()]
    nic_no: constr()
    address: Optional[constr()]
    sex: Sex
    has_vehicle_licence: bool
    registered_date: date
    status: CandidateStatus
