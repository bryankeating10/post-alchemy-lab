"""
Define the schema for all tables in the database
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# Connection string for PostgreSQL
DATABASE_URL = 'postgresql://labuser:labpass@db:5432/sandbox'

# Create an engine
engine = create_engine(DATABASE_URL, echo=False)

# Define the ORM Base
Base = declarative_base()

# Define the RUMS table
class RUMS(Base):
    __tablename__ = 'rums'
    
    id = Column(Integer, primary_key=True)

    # Match details
    datetime = Column(DateTime)
    location = Column(String)
    
    # Competitors
    home_team = Column(String)
    away_team = Column(String)

    # Match statistics
    home_goals = Column(Integer)
    away_goals = Column(Integer)
    home_shots = Column(Integer)
    away_shots = Column(Integer)