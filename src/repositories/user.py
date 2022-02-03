from src.models import db
from src.models.models import User


class UserRepository:
    @staticmethod
    def register_user(nome, email, senha):
        user = User(nome=nome, email=email, senha=senha)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all_users():
        return User.query.all()
