"""
Investigates SQLAlchemy and PostgreSQL interactions:
    - Connect to Postgres
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Connection string for PostgreSQL
DATABASE_URL = 'postgresql://labuser:labpass@db:5432/sandbox'

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)


