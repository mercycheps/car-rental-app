# lib/db/seed.py
from lib.db.models import Car, Customer, Rental, Session
import datetime

def seed():
    session = Session()

    # Add some cars
    car1 = Car(make="Toyota", model="Camry", year=2020)
    car2 = Car(make="Toyota", model="TX", year=2020)
    car3 = Car(make="Honda", model="Civic", year=2019)
    car4 = Car(make="Honda", model="CRV", year=2019)
    car5 = Car(make="Nissan", model="xTrail", year=2019)
    car6 = Car(make="Hyndai", model="Santafe", year=2019)
    car7 = Car(make="Mercedes", model="G Wagon", year=2019)
    car8 = Car(make="Mercedes", model="GLE", year=2019)
    session.add_all([car1, car2, car3, car4, car5, car6, car7, car8])
    session.commit()
    
    # Add some customers
    customer1 = Customer(name="Jim Watkins", address="Ngong Avenue", driving=5)
    session.add(customer1)
    session.commit()
    
    # Add a rental
    rental1 = Rental(car_id=car1.id, customer_id=customer1.id, start_date=datetime.date(2025, 6, 1), end_date=datetime.date(2025, 6, 7))
    session.add(rental1)
    session.commit()

    print("Seed data inserted.")

if __name__ == "__main__":
    seed()
