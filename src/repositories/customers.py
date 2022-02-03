from src.models import db
from src.models.models import Customer


class CustomersRepository:
    @staticmethod
    def register_customer(nome, cpf):
        customer = Customer(nome=nome, cpf=cpf)
        db.session.add(customer)
        db.session.commit()
        return customer

    @staticmethod
    def get_customer_by_cpf(cpf):
        return Customer.query.filter_by(cpf=cpf).first()

    @staticmethod
    def get_all_customers():
        return Customer.query.all()

    @staticmethod
    def get_customer_by_id(id):
        return Customer.query.filter_by(id=id).first()

    @staticmethod
    def update_customer(customer, nome, cpf):
        customer.nome = nome
        customer.cpf = cpf
        db.session.commit()
        return customer

    @staticmethod
    def delete_user(customer):
        db.session.delete(customer)
        db.session.commit()
        return customer