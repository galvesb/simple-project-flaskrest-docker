from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from . import db


@dataclass
class Car(db.Model):

    __tablename__ = "car"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))
    ano = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    customer = relationship("Customer")

    # def __repr__(self) -> str:
    #     return f"Car(nome={self.nome}, customer={self.customer})"


@dataclass
class Customer(db.Model):
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))
    cpf = db.Column(db.String(100), unique=True)
    cars = db.relationship("Car", backref="car", uselist=True)


@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)
