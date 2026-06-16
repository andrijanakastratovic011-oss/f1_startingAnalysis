import pandas as pd
from sqlalchemy import text
from dotenv import load_dotenv
load_dotenv()


def load_dim_date(engine, start='2012-01-01', end='2023-12-31'):
    date_index = pd.date_range(start=start, end=end, freq='D')

    dim_date = pd.DataFrame({
        'dateId': date_index.strftime('%Y%m%d'),
        'date': date_index,
        'day': date_index.day,          
        'month': date_index.month,
        'year': date_index.year,
    })
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE dim_date CASCADE"))
    dim_date.to_sql("dim_date", engine, if_exists='append', index=False)
    return dim_date

def load_dim_race(engine):
    dim_race = pd.read_sql('SELECT DISTINCT "raceId", silver_layer.year, round, race_name, silver_layer.date, races_time, race_url, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time, "dateId" FROM silver_layer INNER JOIN dim_date ON silver_layer.date=dim_date.date', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE dim_race CASCADE"))
    dim_race.to_sql("dim_race", engine, if_exists='append', index=False)
    return dim_race

def load_dim_driver(engine):
    dim_driver = pd.read_sql('SELECT DISTINCT "driverId", "driverRef", drivers_number, code, forename, surname, dob, driver_nationality, driver_url FROM silver_layer', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE dim_driver CASCADE"))
    dim_driver.to_sql("dim_driver", engine, if_exists='append', index=False)
    return dim_driver

def load_dim_status(engine):
    dim_status = pd.read_sql('SELECT DISTINCT "statusId", status FROM silver_layer', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE dim_status CASCADE"))
    dim_status.to_sql("dim_status", engine, if_exists='append', index=False)
    return dim_status

def load_dim_constructor(engine):
    dim_constructor = pd.read_sql('SELECT DISTINCT "constructorId", "constructorRef", constructors_name, constructors_nationality, constructors_url FROM silver_layer', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE dim_constructor CASCADE"))
    dim_constructor.to_sql("dim_constructor", engine, if_exists='append', index=False)
    return dim_constructor

def load_dim_circuit(engine):
    dim_circuit = pd.read_sql('SELECT DISTINCT "circuitId", "circuitRef", circuit_name, location, country, lat, lng, alt, circuit_url FROM silver_layer', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE dim_circuit CASCADE"))
    dim_circuit.to_sql("dim_circuit", engine, if_exists='append', index=False)
    return dim_circuit

def load_dim_driverstandings(engine):
    dim_driverstandings = pd.read_sql('SELECT DISTINCT "driverStandingsId", driverstandings_points, driverstandings_position, "driverstandings_positionText", driverstandings_wins FROM silver_layer', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE dim_driverstandings CASCADE"))
    dim_driverstandings.to_sql("dim_driverstandings", engine, if_exists='append', index=False)
    return dim_driverstandings

def load_dim_constructorstandings(engine):
    dim_constructorstandings = pd.read_sql('SELECT DISTINCT "constructorStandingsId", constructorstandings_points, constructorstandings_position, "constructorstandings_positionText", constructorstandings_wins FROM silver_layer', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE dim_constructorstandings CASCADE"))
    dim_constructorstandings.to_sql("dim_constructorstandings", engine, if_exists='append', index=False)
    return dim_constructorstandings

def load_fact_results(engine):
    fact_results = pd.read_sql('SELECT DISTINCT "resultId", "raceId", "driverId", "constructorId", "statusId", "circuitId", "driverStandingsId", "constructorStandingsId", number, grid, position, "positionText", "positionOrder", points, time, milliseconds, laps, "fastestLap", "fastestLapTime", "fastestLapSpeed", rank FROM silver_layer', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE fact_results"))
    fact_results.to_sql("fact_results", engine, if_exists='append', index=False)
    return fact_results

def load_fact_lap(engine):
    fact_lap = pd.read_sql('SELECT DISTINCT "raceId", "driverId", lap, laptimes_position, laptimes_time, laptimes_milliseconds FROM silver_layer', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE fact_lap"))
    fact_lap.to_sql("fact_lap", engine, if_exists='append', index=False)
    return fact_lap

def load_fact_pitstops(engine):
    fact_pitstops = pd.read_sql('SELECT DISTINCT "raceId", "driverId", stop, pitstops_lap, pitstops_time, duration, pitstops_milliseconds FROM silver_layer', engine)
    with engine.begin() as connection:
        connection.execute(text("TRUNCATE TABLE fact_pitstops"))
    fact_pitstops.to_sql("fact_pitstops", engine, if_exists='append', index=False)
    return fact_pitstops