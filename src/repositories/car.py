from src.models import db
from src.models.models import Car, Customer


class CarsRepository:
    @staticmethod
    def register_car(nome, ano, customer_id):
        car = Car(nome=nome, ano=ano, customer=customer_id)
        db.session.add(car)
        db.session.commit()
        return car

    @staticmethod
    def get_customer_by_id(car_id, customer_id):
        return Car.query.filter(Customer.id == customer_id).filter_by(id=car_id).all()
