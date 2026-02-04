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

