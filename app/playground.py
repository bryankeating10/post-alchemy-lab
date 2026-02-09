"""
Investigates SQLAlchemy and PostgreSQL interactions:
    - Connect to Postgres
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Connection string for PostgreSQL
DATABASE_URL = 'postgresql://labuser:labpass@db:5432/sandbox'

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Define the ORM Base
Base = declarative_base()

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

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add game data
game1 = RUMS(
    datetime=datetime(2023, 9, 12, 19, 0),
    location="Piscataway, NJ",
    home_team="Rutgers",
    away_team="Penn State",
    home_goals=2,
    away_goals=1,
    home_shots=14,
    away_shots=9
)

# Clear existing dat in RUMS table
session.query(RUMS).delete()

# Add the game to the session and commit
session.add(game1)
session.commit()

# Query the database to check if the game was added
games = session.query(RUMS).all()
for game in games:
    print(f'Game ID: {game.id}')
    print(f"{game.datetime} - {game.home_team} vs {game.away_team}: {game.home_goals}-{game.away_goals}")
    print(f'Shots: {game.home_shots} (home) vs {game.away_shots} (away)')

# Better formatting
for game in games:
    print(f'Game ID: {game.id}')
    print(f'After the game in {game.location}, \
          on {game.datetime.strftime("%B %d, %Y at %I:%M %p")}, \
          {game.home_team} and {game.away_team} took {game.home_shots} and {game.away_shots} shots respectively, \
          with a final score of {game.home_goals} to {game.away_goals}.')
    
# Close the session
session.close()