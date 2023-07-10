"""
Name : manage.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 22/06/2023 7:02 AM
Desc: manage.py
"""
import csv
import os.path
import sys
import traceback

import click
from flask.cli import with_appcontext
from sqlalchemy import inspect

from app import VehicleManufacturer
from app.extensions import db
from app.util.custom_commands import CustomCommnds


# create command function
@click.command(name='create_db')
@with_appcontext
def create():
    """Create all database tables."""
    print("Database Creating Process Successfully Started.")
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Database is Successfully Seeded.")


# create command function
@click.command(name='seed_db')
@with_appcontext
def seed_db():
    """Seed data to the database."""
    print("Database Seeding Process Successfully Started.")
    try:
        cc = CustomCommnds(database=db)
        cc.seed_vehicle_manufacturers()

    except Exception as e:
        print(traceback.format_exc())
        print(str(e))
    print("Database is Successfully Seeded.")


# add command function to cli commands
def add_command(app):
    app.cli.add_command(create)
    app.cli.add_command(seed_db)
