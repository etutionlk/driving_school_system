"""
Name : routes.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 21/06/2023 9:42 PM
Desc: routes.py
"""


def register_routes(api):
    from app.candidate import register_candidate
    register_candidate(api)
