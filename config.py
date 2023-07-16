"""
Name : config.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 20/06/2023 10:59 AM
Desc: config.py
"""
import os


class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'do-i-really-need-this'
    FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    FLASK_SECRET = SECRET_KEY
    DB_HOST = 'database'  # a docker link


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG_MODE = bool(os.environ.get("DEBUG_MODE", "True"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:letmein@localhost:3306/driving_school")
