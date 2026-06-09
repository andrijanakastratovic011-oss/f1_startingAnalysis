from load import load_silver
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

if __name__=="__main__":
    load_dotenv()
    
    engine = create_engine(os.getenv("DATABASE_URL"))
    with engine.begin() as conn:
        df = load_silver(conn)
