from pytest import fixture
import pytest

# from slugify import slugify

from main import create_app
from src.models import db
from src.models.models import User


@fixture
def app():
    app = create_app()
    app.testing = True
    return app


@pytest.fixture()
def create_database(app):
    with app.app_context():
        db.create_all()

        yield db

        db.session.remove()
        db.drop_all()


@pytest.fixture(autouse=True)
def makedb(create_database):
    p = User()
    p.nome = "teste user"
    p.email = "email@email.com"
    p.senha = "123"

    db.session.add(p)
    db.session.commit()
