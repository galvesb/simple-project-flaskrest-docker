from flask_restful import fields
from flask_restful.fields import String


customers_fields = {
    "nome": fields.String,
    "cpf": fields.String,
}

car_fields = {
    "id": fields.Integer,
    "nome": fields.String,
    "ano": fields.String,
    "customer": fields.List(fields.Nested(customers_fields)),
}

user_field = {
    "id": fields.Integer,
    "nome": fields.String,
    "email": fields.String,
}