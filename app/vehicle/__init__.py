"""
Name : __init__.py.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 29/06/2023 11:19 PM
Desc: __init__.py.py
"""
from app.vehicle.controller import vehicle


def register_vehicle(api):
    api.add_namespace(vehicle, path="/api")