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

from app import VehicleManufacturer, UserRole, LicenseClass
from app.util import UserStatus

# data files
MANUFACTURER_DATA_CSV_FILE = os.environ.get("MANUFACTURER_DATA_CSV_FILE", "data/car_manufacturers.csv")
USER_ROLE_DATA_CSV_FILE = os.environ.get("USER_ROLE_DATA_CSV_FILE", "data/user_roles.csv")
LICENSE_CLASS_DATA_CSV_FILE = os.environ.get("LICENSE_CLASS_DATA_CSV_FILE", "data/license_classes.csv")


class CustomCommnds:
    """Class for custom flask commands"""

    def __init__(self, database):
        self.db = database

    def seed_user_roles(self):
        try:
            inspector = inspect(self.db.engine)

            if not os.path.isfile(USER_ROLE_DATA_CSV_FILE):
                print(
                    "User Rol csv file is not there. Copy th csv file to data directory and re-run the command")
                return
            if not inspector.has_table("user_role"):
                print(
                    "user_role table is not in the database.Use create_db command to create the database and re-run "
                    "the seed_db command")
                return

            # check data is exists or not
            user_roles = [user.user_role.lower() for user in self.db.session.query(UserRole).all()]

            insert_user_roles = []
            with open(USER_ROLE_DATA_CSV_FILE, 'r') as file:
                csv_reader = csv.reader(file, delimiter=',')
                for row in csv_reader:
                    if row[0].lower() not in user_roles:
                        insert_user_roles.append(UserRole(user_role=row[0], status=UserStatus.ENABLED))

            if len(insert_user_roles) > 0:
                print("Seeding user_role table...")
                self.db.session.add_all(insert_user_roles)
                self.db.session.commit()
            else:
                print("No changes in user_role table.")
        except Exception as e:
            print(traceback.format_exc())
            print(str(e))

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



    def seed_license_class(self):
        try:
            inspector = inspect(self.db.engine)

            if not os.path.isfile(MANUFACTURER_DATA_CSV_FILE):
                print(
                    "License Classes csv file is not there. Copy th csv file to data directory and re-run the command")
                return
            if not inspector.has_table("license_class"):
                print(
                    "license_class table is not in the database.Use create_db command to create the database and "
                    "re-run the seed_db command")
                return

            # check data is exists or not
            classes = [cls.license_class.lower() for cls in self.db.session.query(LicenseClass).all()]

            insert__license_classes = []
            with open(LICENSE_CLASS_DATA_CSV_FILE, 'r') as file:
                csv_reader = csv.reader(file, delimiter='\t')
                for row in csv_reader:
                    if row[1].lower() not in classes:
                        insert__license_classes.append(LicenseClass(license_class=row[1], description=row[0],
                                                                    other_eligible_classes=row[2]))

            if len(insert__license_classes) > 0:
                print("Seeding license_class table...")
                self.db.session.add_all(insert__license_classes)
                self.db.session.commit()
            else:
                print("No changes in license_class table.")
        except Exception as e:
            print(traceback.format_exc())
            print(str(e))

    def seed_all_tables(self):
        self.seed_vehicle_manufacturers()
        self.seed_user_roles()
        self.seed_license_class()
