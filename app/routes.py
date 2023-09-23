"""
Name : routes.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 21/06/2023 9:42 PM
Desc: routes.py
"""
from app.candidate import register_candidate
from app.license_category import register_license_category
from app.trial import register_trial
from app.vehicle import register_vehicle


def register_routes(api):
    register_candidate(api=api)
    register_vehicle(api=api)
    register_license_category(api=api)
    register_trial(api=api)
