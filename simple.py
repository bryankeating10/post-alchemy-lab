"""
Simplest SQLAlchemy use:
    - Connect
    - Create a table
    - Add data
    - Query

Run with:
    python simple.py
"""

# Import dependencies
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Connect to database
engine = create_engine("postgresql://labuser:labpass@db:5432/sandbox")

# Define a base for models
Base = declarative_base()

# Define a simple model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

# Create the table
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()