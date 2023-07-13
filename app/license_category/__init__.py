"""
Name : __init__.py.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 29/06/2023 11:19 PM
Desc: __init__.py.py
"""
from app.license_category.controller import license_category


def register_license_category(api):
    api.add_namespace(license_category, path="/api")