from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from . import Base, Session
from .car import Car
from .customer import Customer
from datetime import date

class Rental(Base):
    __tablename__ = 'rentals'

    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    car = relationship('Car', back_populates='rentals')
    customer = relationship('Customer', back_populates='rentals')

    def __repr__(self):
        return f"<Rental(id={self.id}, car_id={self.car_id}, start_date={self.start_date}, end_date={self.end_date})>"
    
    @classmethod
    def is_car_model_available(cls, make, model, year):
        session = Session()
        #Query cars with matching make, model, year and no rentals
        available_car = (
            session.query(Car)
            .outerjoin(Rental)
            .filter(Car.make == make, Car.model == model, Car.year == year)
            .filter(Rental.id == None)
            .all()
        )
        session.close()
        return available_car is not None
    
    
        # find all cars in cars table matching query
        # join the rental table and return cars that have no rental

        # return False;  
    @classmethod
    def total_cost(self):
        days = (self.end_date - self.start_date) .days
        return days * self.car.rental_price
    
    @classmethod
    def create(cls, car_id, customer_id, start_date, end_date):
        session = Session()
        rental = cls(car_id=car_id, customer_id=customer_id, start_date=start_date, end_date=end_date)
        session.add(rental)
        session.commit()
        session.refresh(rental)
        session.close()
        return rental