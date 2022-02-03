from flask import Flask
from flask_jwt_extended import JWTManager
from src.routes import routes
from src.models import db
from dynaconf import FlaskDynaconf


app = Flask(__name__)


def create_app():

    FlaskDynaconf(app)
    db.init_app(app)
    JWTManager(app)
    routes.init_app(app)

    return app


if __name__ == "__main__":

    create_app().run(debug=True, host="0.0.0.0")
