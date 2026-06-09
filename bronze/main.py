from load import load_bronze
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

if __name__=="__main__":
    load_dotenv()
    csv_name=os.getenv("CSV_NAME")
    engine = create_engine(os.getenv("DATABASE_URL"))
    with engine.begin() as conn:
        load_bronze(csv_name, conn)
