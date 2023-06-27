"""
Name : manage.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 22/06/2023 7:02 AM
Desc: manage.py
"""
import click
from flask.cli import with_appcontext
from app.extensions import db


# create command function
@click.command(name='create')
@with_appcontext
def create():
    """Create all database tables."""
    print("Database Seeding Process Successfully Started.")
    db.drop_all()
    # db.session.add(User("root", "root@etutionlk.com"))
    db.create_all()
    db.session.commit()
    print("Database is Successfully Seeded.")


# add command function to cli commands
def add_command(app):
    app.cli.add_command(create)
