"""
Name : __init__.py.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 29/06/2023 6:30 AM
Desc: __init__.py.py
"""
import enum


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
