import logging
from flask_restful import Resource, marshal_with
from flask import request
from src.repositories.user import UserRepository
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required
from src.resources.schemas import user_field


class User(Resource):
    def post(self):
        user = request.get_json()
        print(user)
        nome = user.get("nome")
        email = user.get("email")
        senha = user.get("senha")

        try:
            user = UserRepository.get_user_by_email(email)
            print(user)

            if user:
                return {"Error": "E-mail já cadastrado"}, 400

            UserRepository.register_user(
                nome=nome,
                email=email,
                senha=generate_password_hash(senha, salt_length=5),
            )

            return {"message": "usuário cadastrado com sucesso"}, 200
        except Exception as e:
            # db.session.rollback()
            logging.critical(str(e))
            return {"error": "não foi possível criar o seu pedido"}, 500

    @jwt_required
    @marshal_with(user_field, "users")
    def get(self):
        users = UserRepository.get_all_users()
        return users


class Login(Resource):
    def post(self):

        user = request.get_json()
        email = user.get("email")
        senha = user.get("senha")

        user = UserRepository.get_user_by_email(email)

        if not user or not check_password_hash(user.senha, senha):
            return {"error": "login e senha invalidos"}, 400

        token = create_access_token(
            {"id": user.id}, expires_delta=timedelta(minutes=15)
        )

        return {"access_token": token}
