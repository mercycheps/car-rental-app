# 🚗 Car Rental CLI App

A command-line application for managing a car rental service. Built with Python, SQLAlchemy, Alembic, and SQLite.

---

## 📦 Features

- List all cars
- Find car by ID
- Create, update, delete cars
- Seed initial data
- Easily extendable to handle customers, rentals, etc.

---

## 🛠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mercycheps/car-rental-app.git
cd car-rental-app
```

## 2. Install dependencies
We use Pipenv for dependency management:

```bash
pipenv install
pipenv shell
```

## 3. Initialize the database
Make sure Alembic is initialized

```bash
alembic upgrade head
```

### 🌱 Seed the database

```bash
python seeds.py
```

## 🚀 Run the CLI

Once the setup is complete, run the interactive CLI with:

```bash
python -m lib.cli

--- Car Rental CLI ---
1. List all cars
2. Find car by ID
3. Create new car
4. Update existing car
5. Delete a car
6. Exit
Select an option: 
```
