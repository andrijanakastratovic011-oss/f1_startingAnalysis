from load import load_bronze
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

if __name__=="__main__":
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    df = load_bronze(engine)
    print(f"Bronze učitano: {len(df)} redova")