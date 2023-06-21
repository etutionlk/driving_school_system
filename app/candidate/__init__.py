"""
Name : __init__.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 20/06/2023 8:21 AM
Desc: __init__.py
"""
from app.candidate.controller import candidate


def register_candidate(api):
    api.add_namespace(candidate, path="/candidate")


# https://www.youtube.com/watch?v=Qf0wri9MvMY&ab_channel=PrettyPrinted
# https://github.com/PrettyPrinted/youtube_video_code/tree/master/2023/05/01/How%20to%20Easily%20Create%20REST%20APIs%20with%20Flask-RESTX/flask_restx_example/app