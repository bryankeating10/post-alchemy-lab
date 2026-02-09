"""
Define the schema for all tables in the database
"""

from sqlalchemy import create_engine, inspect, Column, Integer, String, DateTime
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
    date = Column(DateTime)
    location = Column(String)
    
    # Competitors
    home_team = Column(String)
    away_team = Column(String)

    # Match statistics
    home_goals = Column(Integer)
    away_goals = Column(Integer)
    home_shots = Column(Integer)
    away_shots = Column(Integer)

# Define the WalmartSales table
class WalmartSales(Base):
    __tablename__ = "walmart_sales"

    id = Column(Integer, primary_key=True)

    # Internal factors
    Store = Column(String)
    Date = Column(DateTime)
    Weekly_Sales = Column(Integer)

    # External factors
    Holiday_Flag = Column(Integer)
    Temperature = Column(Integer)
    Fuel_Price = Column(Integer)
    CPI = Column(Integer)
    Unemployment = Column(Integer)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables in database
Base.metadata.create_all(engine)

# Verify tables created
inspector = inspect(engine)
print(inspector.get_table_names())

# Close the session
session.close()