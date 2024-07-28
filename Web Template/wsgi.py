import click
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.database import create_db, get_migrate
from App.main import create_app

# This commands file allow you to create convenient CLI commands for testing controllers
app = create_app()
migrate = get_migrate(app)
# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

#Generic Commands

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

@app.cli.command("run")
def initialize():
    print('hello')