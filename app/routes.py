"""
Name : routes.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 21/06/2023 9:42 PM
Desc: routes.py
"""
from app.candidate import register_candidate
from app.vehicle import register_vehicle


def register_routes(api):
    register_candidate(api)
    register_vehicle(api)
