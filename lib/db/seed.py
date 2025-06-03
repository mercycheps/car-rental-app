# lib/db/seed.py
from lib.db.models import  Car, Customer, Rental
from .models import Session
import datetime 

def seed():
    session = Session()
    

    # Add some cars
    car1 = Car(make="Toyota", model="Camry", year=2020, rental_price=8000)
    car2 = Car(make="Toyota", model="TX", year=2020, rental_price=4000)
    car3 = Car(make="Honda", model="Civic", year=2019, rental_price=7000)
    car4 = Car(make="Honda", model="CRV", year=2019, rental_price=2000)
    car5 = Car(make="Nissan", model="xTrail", year=2019, rental_price=4500)
    car6 = Car(make="Hyndai", model="Santafe", year=2019, rental_price=7000)
    car7 = Car(make="Mercedes", model="G Wagon", year=2019, rental_price=15000)
    car8 = Car(make="Mercedes", model="GLE", year=2019, rental_price=20000)
    
    # for car_data in cars:
    #     existing = session.query(Car).filter_by(make=car_data["make"], model=car_data["model"]).first()
    #     if not existing:
    #         session.add(Car(**car_data))
    #     else:
    #         print(f"Skipped duplicate: {car_data['make']} {car_data['model']}")


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
