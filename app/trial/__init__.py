"""
Name : __init__.py.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 29/06/2023 11:21 PM
Desc: __init__.py.py
"""

from app.trial.controller import trial


def register_trial(api):
    api.add_namespace(trial, path="/api")
