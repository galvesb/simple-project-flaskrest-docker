from flask_restful import Api
from src.resources import user, customers, car


def init_app(app):
    api = Api(app, prefix="/api")

    api.add_resource(user.User, "/users")
    api.add_resource(user.Login, "/auth/login")

    api.add_resource(customers.RegisterCustomer, "/register/customer")
    api.add_resource(customers.ListAllCustomers, "/customers")
    api.add_resource(customers.Customer, "/customer/<customer_id>")

    api.add_resource(car.RegisterCar, "/register/car")
    api.add_resource(car.Car, "/car/<car_id>/customer/<customer_id>")
