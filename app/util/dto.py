"""
Name : dto.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 02/07/2023 7:55 PM
Desc: dto.py
"""
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, constr, field_validator
from app.util import Sex, CandidateStatus, Title, Status


class CandidateDTO(BaseModel):
    title: Title
    fullname: constr()
    date_of_birth: date
    mobile_no_1: constr()
    mobile_no_2: Optional[constr()] = None
    nic_no: constr()
    address: Optional[constr()] = None
    sex: Sex
    has_vehicle_license: bool
    registered_date: datetime
    status: CandidateStatus


class CandidateUpdateDTO(BaseModel):
    title: Optional[Title] = None
    fullname: Optional[constr()] = None
    date_of_birth: Optional[date] = None
    mobile_no_1: Optional[constr()] = None
    mobile_no_2: Optional[constr()] = None
    nic_no: Optional[constr()] = None
    address: Optional[constr()] = None
    sex: Optional[Sex] = None
    has_vehicle_license: Optional[bool] = None

    @field_validator("title", mode="before")
    def title_validation(cls, value):
        value = value.replace(".", "").upper()
        if value in Title._member_names_:
            return Title[value]
        else:
            raise ValueError("Rev. Mr. Mrs. Ms.")


class VehicleDTO(BaseModel):
    model: constr(min_length=3)
    registration_no: constr(min_length=4)
    manufacturer_id: int


class VehicleUpdateDTO(BaseModel):
    model: constr(min_length=3) = None
    registration_no: constr(min_length=4) = None
    manufacturer_id: Optional[int] = None


class LicenseCategoryDTO(BaseModel):
    license_class_id: int
    description: constr()
    skilled_category_fee: float
    unskilled_category_fee: float
    skilled_no_of_lessons: int
    unskilled_no_of_lessons: int
    status: Status = Status.ENABLED

