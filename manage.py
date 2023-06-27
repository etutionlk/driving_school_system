"""
Name : manage.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 22/06/2023 7:02 AM
Desc: manage.py
"""
import click
from flask.cli import with_appcontext


# create command function
@click.command(name='create')
@with_appcontext
def create(db):
    """Create all database tables."""
    print("hello")
    db.create_all()


# add command function to cli commands
def add_command(app):
    app.cli.add_command(create)
