from load import load_dim_race, load_dim_driver, load_dim_circuit, load_dim_constructor, load_dim_constructorstandings, load_dim_driverstandings, load_dim_status, load_fact_results, load_fact_lap, load_fact_pitstops, load_dim_date
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from gold.model import Base

if __name__=="__main__":
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    Base.metadata.create_all(engine)

    load_dim_date(engine)
    load_dim_race(engine)
    load_dim_driver(engine)
    load_dim_status(engine)
    load_dim_constructor(engine)
    load_dim_circuit(engine)
    load_dim_driverstandings(engine)
    load_dim_constructorstandings(engine)
    load_fact_results(engine)
    load_fact_lap(engine)
    load_fact_pitstops(engine)
