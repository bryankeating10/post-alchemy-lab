"""
Practice using KaggleAPI to download datasets and pandas
to insert data into a PostgreSQL database.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

import pandas as pd

from kaggle.api.kaggle_api_extended import KaggleApi

# Download dataset using Kaggle API
api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    'mikhail1681/walmart-sales',
    path='/app/data',
    unzip=True
)