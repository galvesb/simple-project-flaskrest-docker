from gc import get_objects
import logging
from flask_restful import Resource, marshal_with
from flask import request
from flask_jwt_extended import jwt_required
from src.resources.schemas import customers_fields
from src.repositories.customers import CustomersRepository


class RegisterCustomer(Resource):
    @jwt_required
    def post(self):
        customer = request.get_json()
        nome = customer.get("nome")
        cpf = customer.get("cpf")

        try:
            customer = CustomersRepository.get_customer_by_cpf(cpf)

            if customer:
                return {"message": "Cliente já cadastrado"}, 400

            CustomersRepository.register_customer(nome=nome, cpf=cpf)
            return {"message": "Cliente cadastrado com sucesso!"}, 201
        except Exception as e:
            logging.critical(str(e))
            return {"Error": "Não foi possível cadastrar o cliente"}, 500


class ListAllCustomers(Resource):
    @jwt_required
    @marshal_with(customers_fields, "customers")
    def get(self):
        customers = CustomersRepository.get_all_customers()
        return customers


class Customer(Resource):
    @jwt_required
    @marshal_with(customers_fields, "customer")
    def get(self, customer_id):
        customer = CustomersRepository.get_customer_by_id(id=customer_id)
        print(customer)
        return customer

    @jwt_required
    def put(self, customer_id):
        customer = request.get_json()
        nome = customer.get("nome")
        cpf = customer.get("cpf")

        customer = CustomersRepository.get_customer_by_id(id=customer_id)

        customer_already_exist = CustomersRepository.get_customer_by_cpf(cpf)

        if customer_already_exist:
            return {"message": "Cliente já cadastrado"}, 400

        CustomersRepository.update_customer(customer, nome, cpf)

        return {"message": "Cliente alterado"}

    @jwt_required
    def delete(self, customer_id):
        customer = CustomersRepository.get_customer_by_id(customer_id)

        CustomersRepository.delete_user(customer)

        return {"message": "Cliente deletado"}, 200
