from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from . import Base, Session


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    driving = Column(Integer, nullable=False)
    rentals = relationship('Rental', back_populates='customer', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name}, address={self.address}, driving={self.driving})>"

    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        car = session.query(cls).filter_by(id=id_).first()
        session.close()
        return car

    @classmethod
    def get_all(cls):
        session = Session()
        cars = session.query(cls).all()
        session.close()
        return cars

    @classmethod
    def create(cls, make, model, year):
        session = Session()
        car = cls(make=make, model=model, year=year)
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
