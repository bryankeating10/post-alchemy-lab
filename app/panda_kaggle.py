"""
Practice using KaggleAPI to download datasets and pandas
to insert data into a PostgreSQL database.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

from table_creation import Session, WalmartSales

# Download dataset using Kaggle API
api = KaggleApi()
api.authenticate()
print('Authenticated API')

api.dataset_download_files(
    'mikhail1681/walmart-sales',
    path='/app/data',
    unzip=True
)
print('Downloaded sales data')

df = pd.read_csv('/app/data/Walmart_Sales.csv')
print(df.head())

# Open a session
session = Session()