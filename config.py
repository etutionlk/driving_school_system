"""
Name : config.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 20/06/2023 10:59 AM
Desc: config.py
"""


class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'do-i-really-need-this'
    FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    FLASK_SECRET = SECRET_KEY
    DB_HOST = 'database'  # a docker link


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:letmein@localhost/driving_school'
