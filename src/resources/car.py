import imp
import logging
from flask_restful import Resource, marshal_with
from src.resources.schemas import car_fields
from flask import request
from flask_jwt_extended import jwt_required

from src.repositories.car import CarsRepository
from src.repositories.customers import CustomersRepository


class RegisterCar(Resource):
    @jwt_required
    def post(self):
        customer = request.get_json()
        nome = customer.get("nome")
        ano = customer.get("ano")
        custumer_id = customer.get("customer_id")

        try:
            customer = CustomersRepository.get_customer_by_id(id=custumer_id)
            CarsRepository.register_car(nome=nome, ano=ano, customer_id=customer)
            return {"message": "Carro cadastrado com sucesso!"}, 201
        except Exception as e:
            logging.critical(str(e))
            return {"Error": "Não foi possível cadastrar o Carro"}, 500


class Car(Resource):
    @jwt_required
    @marshal_with(car_fields, "cars")
    def get(self, car_id, customer_id):
        try:
            cars = CarsRepository.get_customer_by_id(
                car_id=car_id, customer_id=customer_id
            )
            return cars
        except Exception as e:
            logging.critical(str(e))
            return {"Error": "Não foi possível cadastrar o Carro"}, 500
