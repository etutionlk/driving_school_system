"""
Name : exceptions.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 06/07/2023 5:22 AM
Desc: exceptions.py
"""


class NoResultFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super(NoResultFoundException, self).__init__(self.message)

    def __str__(self):
        return self.message
