from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import UniqueConstraint, Column, Integer, String, ForeignKey, Date, Float
from . import Base, Session


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rental_price = Column(Float, nullable=True)

    rentals = relationship('Rental', back_populates='car', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Car(id={self.id}, make={self.make}, model={self.model}, year={self.year}, rental_price={self.rental_price})>"

    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        car = session.query(cls).filter_by(id=id_).first()
        session.close()
        return car
    
    @classmethod
    def find_by_make_model_price(cls, make, model, rental_price):
        session = Session()
        car = session.query(cls).filter_by(make=make, model=model, rental_price=rental_price).first()
        session.close()
        return car

    @classmethod
    def get_all(cls):
        session = Session()
        cars = session.query(cls).all()
        session.close()
        return cars

    @classmethod
    def create(cls, make, model, year, rental_price):
        session = Session()
        car = cls(make=make, model=model, year=year, rental_price=rental_price)
        session.add(car)
        session.commit()
        session.refresh(car)
        session.close()
        return car

    def update(self):
        session = Session()
        session.merge(self)
        session.commit()
        session.close()

    def delete(self):
        session = Session()
        session.delete(self)
        session.commit()
        session.close()
