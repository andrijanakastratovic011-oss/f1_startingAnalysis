import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from model import Base 
load_dotenv()

def load_dim_race(engine):
    Base.metadata.create_all(engine)
    dim_race = pd.read_sql("SELECT 'raceId', year, round, date, time_races, url_x, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS dim_race CASCADE"))
        connection.commit()
    dim_race.to_sql("dim_race", engine, if_exists='append', index=False)
    return dim_race

def load_dim_driver(engine):
    Base.metadata.create_all(engine)
    dim_driver = pd.read_sql("SELECT 'driverId', 'driverRef', number_drivers, code, forename, surname, dob, nationality, url FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS dim_driver CASCADE"))
        connection.commit()
    dim_driver.to_sql("dim_driver", engine, if_exists='append', index=False)
    return dim_driver

def load_dim_status(engine):
    Base.metadata.create_all(engine)
    dim_status = pd.read_sql("SELECT 'statusId', status FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS dim_status CASCADE"))
        connection.commit()
    dim_status.to_sql("dim_status", engine, if_exists='append', index=False)
    return dim_status

def create_dim_date(start='2012-01-01', end='2023-12-31'):
    date_index = pd.date_range(start=start, end=end, freq='D')

    dim_date = pd.DataFrame({
        'Date': date_index,
        'Day': date_index.day_name(),          
        'Month': date_index.month,
        'Year': date_index.year,
    })
    dim_date.index.name = 'date_id'
    return dim_date

def load_dim_constructor(engine):
    Base.metadata.create_all(engine)
    dim_constructor = pd.read_sql("SELECT 'constructorId', 'constructorRef', name, nationality_constructors, url_constructors FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS dim_constructor CASCADE"))
        connection.commit()
    dim_constructor.to_sql("dim_constructor", engine, if_exists='append', index=False)
    return dim_constructor

def load_dim_circuit(engine):
    Base.metadata.create_all(engine)
    dim_circuit = pd.read_sql("SELECT 'circuitId', 'circuitRef', name_y, location, country, lat, lng, alt, url_y FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS dim_circuit CASCADE"))
        connection.commit()
    dim_circuit.to_sql("dim_circuit", engine, if_exists='append', index=False)
    return dim_circuit

def load_dim_driverstandings(engine):
    Base.metadata.create_all(engine)
    dim_driverstandings = pd.read_sql("SELECT 'driverStandingsId', 'points_driverStandings', 'position_driverStandings', 'positionText_driverStandings', wins FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS dim_driverstandings CASCADE"))
        connection.commit()
    dim_driverstandings.to_sql("dim_driverstandings", engine, if_exists='append', index=False)
    return dim_driverstandings

def load_dim_constructorstandings(engine):
    Base.metadata.create_all(engine)
    dim_constructorstandings = pd.read_sql("SELECT 'constructorStandingsId', points_constructorstandings, position_constructorstandings, 'positionText_constructorstandings', wins_constructorstandings FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS dim_constructorstandings CASCADE"))
        connection.commit()
    dim_constructorstandings.to_sql("dim_constructorstandings", engine, if_exists='append', index=False)
    return dim_constructorstandings

def load_fact(engine):
    Base.metadata.create_all(engine)
    fact = pd.read_sql("SELECT 'resultId', 'raceId', 'driverId', 'constructorId', 'statusId', 'circuitId', 'driverStandingsId', 'constructorStandingsId', 'dateId', number, grid, position, 'positionText', 'positionOrder', points, time, milliseconds, laps, 'fastestLap', 'fastestLapTime', 'fastestLapSpeed', rank FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS fact"))
        connection.commit()
    fact.to_sql("fact", engine, if_exists='append', index=False)
    return fact

def load_fact_lap(engine):
    Base.metadata.create_all(engine)
    fact_lap = pd.read_sql("SELECT 'raceId', 'driverId', position_laptimes, time_laptimes, milliseconds_laptimes FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS fact_lap"))
        connection.commit()
    fact_lap.to_sql("fact_lap", engine, if_exists='append', index=False)
    return fact_lap

def load_fact_pitstops(engine):
    Base.metadata.create_all(engine)
    fact_pitstops = pd.read_sql("SELECT 'raceId', 'driverId', stop, lap_pitstops, time_pitstops, duration, milliseconds_pitstops FROM silver_layer", engine)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS fact_pitstops"))
        connection.commit()
    fact_pitstops.to_sql("fact", engine, if_exists='append', index=False)
    return fact_pitstops