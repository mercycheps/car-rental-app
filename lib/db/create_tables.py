# lib/db/create_tables.py

from lib.db.models import Base, engine

def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
