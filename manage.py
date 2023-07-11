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
@click.option("--all_tables", default=False, show_default=True, is_flag=True, help="Seed all the tables")
@click.option("--table", default="all", show_default=True, is_flag=False,
              help="Seed table like vehicle_manufacturer, user_role")
@with_appcontext
def seed_db(all_tables, table="all"):
    """Seed data to the database."""
    print("Database Seeding Process Successfully Started.")
    try:
        if not all_tables and table == "":
            print("No options were set. Valid options are --all, --table")

        cc = CustomCommnds(database=db)
        if table == "vehicle_manufacturer":
            cc.seed_vehicle_manufacturers()
        elif table == "user_role":
            cc.seed_user_roles()
        elif table != "all":
            print("Invalid value for --table. valid values are vehicle_manufacturer, user_role")

        if all_tables:
            cc.seed_all_tables()

    except Exception as e:
        print(traceback.format_exc())
        print(str(e))
    print("Database is Successfully Seeded.")


# add command function to cli commands
def add_command(app):
    app.cli.add_command(create)
    app.cli.add_command(seed_db)
