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
# print(df.head())

# Insert DataFrame into PostgreSQL
df.to_sql(
    'walmart_sales',
    engine,
    if_exists='replace',
    index=False
)

"""
# Verify insertion
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM walmart_sales " \
    "LIMIT 10;"))
    for row in result:
        print(row)
"""

# Average weekly sales
with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT AVG("Weekly_Sales") AS avg_sales
        FROM walmart_sales
    """))
    avg_sales = result.scalar()
    print("Average Weekly Sales:", avg_sales)

# Average unemployment
with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT AVG("Unemployment") AS avg_unemp
        FROM walmart_sales
    """))
    avg_unemp = result.scalar()
    print("Average Unemployment:", avg_unemp)

# Average weekly sales relative to unemployment
with engine.connect() as conn:
    result = conn.execute(text(f"""
        SELECT AVG("Weekly_Sales") as unemp_avg_sales
        FROM walmart_sales
        WHERE "Unemployment" < {avg_unemp}
    """))
    below_unemp_avg_sales = result.scalar()
    print("Average weekly sales during below average unemployment:", below_unemp_avg_sales)

with engine.connect() as conn:
    result = conn.execute(text(f"""
        SELECT AVG("Weekly_Sales") as unemp_avg_sales
        FROM walmart_sales
        WHERE "Unemployment" > {avg_unemp}
    """))
    above_unemp_avg_sales = result.scalar()
    print("Average weekly sales during above average unemployment:", above_unemp_avg_sales)