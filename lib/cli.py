from lib.db.models.car  import Car
from lib.db.models.customer  import Customer
from lib.db.models.rental  import Rental
from lib.helpers import exit_program, invalid_option

from datetime import datetime


def list_cars():
    cars = Car.get_all()
    if cars:
        for car in cars:
            print(car)
    else:
        print("No cars found.")

def find_car_by_id():
    try:
        id_ = int(input("Enter the car's ID: "))
        car = Car.find_by_id(id_)
        if car:
            print(car)
        else:
            print(f"Car with ID {id_} not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def create_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")
    rental_price = float(input("Enter rental price per day:"))
   

    try:
        car = Car.create(make, model, int(year), float(rental_price))
        print(f"Car created successfully: {car}")
    except ValueError:
        print("Year must be a number.")
    except Exception as exc:
        print("Error creating car:", exc)

def update_car():
    try:
        id_ = int(input("Enter the car's ID to update: "))
        car = Car.find_by_id(id_)
        if car:
            make = input(f"Enter new make ({car.make}): ") or car.make
            model = input(f"Enter new model ({car.model}): ") or car.model
            year_input = input(f"Enter new year ({car.year}): ")
            year = int(year_input) if year_input else car.year
            rental_price = float(input("Enter rental price per day:"))

            car.make = make
            car.model = model
            car.year = year
            car.rental_price = rental_price
            car.update()

            print(f"Car updated successfully: {car}")
        else:
            print(f"No car found with ID {id_}")
    except ValueError:
        print("Invalid input. ID and year must be numbers.")
    except Exception as e:
        print("Error updating car:", e)

def delete_car():
    try:
        id_ = int(input("Enter the car's ID to delete: "))
        car = Car.find_by_id(id_)
        if car:
            car.delete()
            print(f"Car with ID {id_} deleted.")
        else:
            print(f"No car found with ID {id_}")
    except ValueError:
        print("Invalid ID. Please enter a number.")
        
def rent_car():
    try:
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        rental_price = input("Enter Price: ")
        
        car = Car.find_by_make_model_price(make, model, rental_price)

        if car == None:
            print("Car not found that matches pereference")
            return
        
        
        
        print(f"Car found id={car.id}, make={car.make}, model={car.model}, rental_price={car.rental_price}")
        
        start_date = input("Enter start_date: ")
        end_date = input("Enter end_date: ")
        
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        
        customer_id = int(input("Enter the custmers's ID who wants to rent:"))
        
        customer = Customer.find_by_id(customer_id)
        
        if customer: 
            Rental.create(car.id, customer.id, start_date, end_date)
            print(f"Car rented")
        else:
            print(f"No car found")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def main_menu():
    while True:
        print("\n--- Car Rental CLI ---")
        print("1. List all cars")
        print("2. Find car by ID")
        print("3. Create new car")
        print("4. Update existing car")
        print("5. Delete a car")
        print("6. Rent a car")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            list_cars()
        elif choice == "2":
            find_car_by_id()
        elif choice == "3":
            create_car()
        elif choice == "4":
            update_car()
        elif choice == "5":
            delete_car()
        elif choice == "6":
            rent_car()
        elif choice == "7":
            exit_program()
        else:
            invalid_option(choice)

if __name__ == "__main__":
    main_menu()
