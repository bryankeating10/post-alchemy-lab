"""
Practice using KaggleAPI to download datasets and pandas
to insert data into a PostgreSQL database.
"""

from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

from table_creation import Session, WalmartSales, engine

# Download dataset using Kaggle API
api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    'mikhail1681/walmart-sales',
    path='/app/data',
    unzip=True
)

df = pd.read_csv('/app/data/Walmart_Sales.csv')
print(df.head())

# Insert DataFrame into PostgreSQL
df.to_sql(
    'walmart_sales',
    engine,
    if_exists='replace',
    index=False
)

# Verify insertion
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM walmart_sales;"))
    for row in result:
        print(row)