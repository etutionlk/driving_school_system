"""
Name : custom_commands.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 10/07/2023 8:03 AM
Desc: custom_commands.py
"""
import csv
import os
import traceback

from sqlalchemy import inspect

from app import VehicleManufacturer

# data files
MANUFACTURER_DATA_CSV_FILE = os.environ.get("MANUFACTURER_DATA_CSV_FILE", "data/car_manufacturers.csv")


class CustomCommnds:
    """Class for custom flask commands"""

    def __init__(self, database):
        self.db = database

    def seed_vehicle_manufacturers(self):
        try:
            inspector = inspect(self.db.engine)

            if not os.path.isfile(MANUFACTURER_DATA_CSV_FILE):
                print(
                    "Car Manufacturer csv file is not there. Copy th csv file to data directory and re-run the command")
                return
            if not inspector.has_table("vehicle"):
                print(
                    "vehicle table is not in the database.Use create_db command to create the database and re-run the "
                    "seed_db command")
                return

            # check data is exists or not
            manufacturers = [m.manufacturer.lower() for m in self.db.session.query(VehicleManufacturer).all()]

            insert_manufacturers = []
            with open(MANUFACTURER_DATA_CSV_FILE, 'r') as file:
                csv_reader = csv.reader(file, delimiter=',')
                for row in csv_reader:
                    if row[0].lower() not in manufacturers:
                        insert_manufacturers.append(VehicleManufacturer(manufacturer=row[0]))

            if len(insert_manufacturers) > 0:
                print("Seeding vehicle_manufacturer table...")
                self.db.session.add_all(insert_manufacturers)
                self.db.session.commit()
            else:
                print("No changes in vehicle_manufacturer table.")
        except Exception as e:
            print(traceback.format_exc())
            print(str(e))
