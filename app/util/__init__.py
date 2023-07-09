"""
Name : __init__.py.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 29/06/2023 6:30 AM
Desc: __init__.py.py
"""
import enum


class Title(enum.Enum):
    MR = "Mr."
    MRS = "Mrs."
    MISS = "Miss."
    MS = "Ms."
    REV = "Rev."

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class Sex(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NOT_SPECIFIED = "NOT_SPECIFIED"


class CandidateStatus(enum.Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ON_HOLD = "ON_HOLD"


class PaymentMode(enum.Enum):
    ADMISSION_FEE = "ADMISSION_FEE"
    INDIVIDUAL_LESSON = "INDIVIDUAL_LESSON"
    TRIAL_DATE = "TRIAL_DATE"
    LICENCE_INSTALMENT = "LICENCE_INSTALMENT"


class LessonStatus(enum.Enum):
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    POSTPONED = "POSTPONED"
    ABSENT = "ABSENT"


class Status(enum.Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ExamStatus(enum.Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"
    ABSENT = "ABSENT"
    POSTPONED = "POSTPONED"


class UserStatus(enum.Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ON_HOLD = "ON_HOLD"


class VehicleStatus(enum.Enum):
    WORKING = "WORKING"
    NOT_WORKING = "NOT_WORKING"
    ON_SERVICING = "ON_SERVICING"
    SOLD = "SOLD"
