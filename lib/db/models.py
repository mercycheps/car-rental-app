from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float

Base = declarative_base()
engine = create_engine("sqlite:///lib/db/app.db")
Session = sessionmaker(bind=engine)


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rentals = relationship('Rental', back_populates='car', cascade="all, delete-orphan")
    

    def __repr__(self):
        return f"<Car(id={self.id}, make={self.make}, model={self.model}, year={self.year}, price={self.Rental_price})>"

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


class Rental(Base):
    __tablename__ = 'rentals'

    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    car = relationship('Car', back_populates='rentals')

    def __repr__(self):
        return f"<Rental(id={self.id}, car_id={self.car_id}, start_date={self.start_date}, end_date={self.end_date})>"


    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        rental = session.query(cls).filter_by(id=id_).first()
        session.close()
        return rental
    

    @classmethod
    def get_all(cls):
        session = Session()
        rentals = session.query(cls).all()
        session.close()
        return rentals
    

    @classmethod
    def create(cls, car_id, start_date, end_date):
        session = Session()
        rental = cls(car_id=car_id, start_date=start_date, end_date=end_date)
        session.add(rental)
        session.commit()
        session.refresh(rental)
        session.close()
        return rental

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
