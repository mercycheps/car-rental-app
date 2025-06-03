from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine("sqlite:///car_rental.db")
Session = sessionmaker(bind=engine)

from .car import Car
from .customer import Customer
from .rental import Rental