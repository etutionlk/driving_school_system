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
        inspector = inspect(db.engine)
        CSV_FILE = "data/car_manufacturers.csv"

        if not os.path.isfile(CSV_FILE):
            print("Car Manufacturer csv file is not there. Copy th csv file to data directory and re-run the command")
            return
        if not inspector.has_table("vehicle"):
            print("vehicle table is not in the database.Use create_db command to create the database and re-run the "
                  "seed_db command")
            return

        # check data is exists or not
        manufacturers = [m.manufacturer.lower() for m in db.session.query(VehicleManufacturer).all()]

        insert_manufacturers = []
        with open("data/car_manufacturers.csv", 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                if row[0].lower() not in manufacturers:
                    insert_manufacturers.append(VehicleManufacturer(manufacturer=row[0]))

        if len(insert_manufacturers) > 0:
            print("Seeding vehicle_manufacturer table...")
            db.session.add_all(insert_manufacturers)
            db.session.commit()
        else:
            print("No changes in vehicle_manufacturer table.")

    except Exception as e:
        print(traceback.format_exc())
        print(str(e))
    print("Database is Successfully Seeded.")


# add command function to cli commands
def add_command(app):
    app.cli.add_command(create)
    app.cli.add_command(seed_db)
