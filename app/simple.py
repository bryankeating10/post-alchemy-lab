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

# Add a new user
new_user = User(name='Colette')
session.add(new_user)
session.commit()

# Query the data
users = session.query(User).all()
for user in users:
    print(f'User {user.id}: {user.name}')

# Close the session
session.close()

print('Done! Check the "users" table in your database.')