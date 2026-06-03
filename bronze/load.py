import pandas as pd
from sqlalchemy import text
from dotenv import load_dotenv
from model import Base

load_dotenv()
def load_bronze(csv_name,engine):
    Base.metadata.create_all(engine)
    bronze_layer=pd.read_csv(csv_name, low_memory=False)
    with engine.connect() as connection:
        connection.execute(text("TRUNCATE TABLE bronze_layer"))
        connection.commit()
    bronze_layer.to_sql("bronze_layer", engine, if_exists='append', index=False)
    return bronze_layer