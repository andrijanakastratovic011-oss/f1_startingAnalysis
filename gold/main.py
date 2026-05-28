from load import load_dim_race, load_dim_driver, load_dim_circuit, load_dim_constructor, load_dim_constructorstandings, load_dim_driverstandings, load_dim_status, load_fact, load_fact_lap, load_fact_pitstops, create_dim_date
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

if __name__=="__main__":
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))

    dim_race = load_dim_race(engine)
    dim_driver=load_dim_driver(engine)
    dim_status=load_dim_status(engine)
    dim_date=create_dim_date
    dim_constructor=load_dim_constructor(engine)
    dim_circuit=load_dim_circuit(engine)
    dim_driverstandings=load_dim_driverstandings(engine)
    dim_constructorstandings=load_dim_constructorstandings(engine)
    fact=load_fact(engine)
    fact_lap=load_fact_lap(engine)
    fact_pitstops=load_fact_pitstops(engine)
