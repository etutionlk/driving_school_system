"""
Name : application.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 20/06/2023 8:21 AM
Desc: application.py
"""
from app.candidate.controller import candidate


def register_candidate(api):
    api.add_namespace(candidate, path="/candidate")
