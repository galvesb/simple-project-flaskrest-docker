from src.models import db

from main import app
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# from main import create_app
from dynaconf import FlaskDynaconf

# app = Flask(__name__)
FlaskDynaconf(app)
db.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()