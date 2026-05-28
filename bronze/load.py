import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
from model import Base, Bronze

load_dotenv()
def load_bronze(engine):
    Base.metadata.create_all(engine)
    bronze_layer=pd.read_csv('dataEngineeringDataset.csv', low_memory=False)
    with engine.connect() as connection:
        connection.execute(text("TRUNCATE TABLE bronze_layer"))
        connection.commit()
    bronze_layer.to_sql("bronze_layer", engine, if_exists='append', index=False)
    return bronze_layer