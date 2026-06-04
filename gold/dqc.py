from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

def dataQualityChecksDim(df, id):
    print(f"Redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe is empty.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")

def dataQualityChecksFactResults(df, id):
    print(f"Fact redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe fact_result is empty.")
    #if (df['fastestLap']>df['laps']).any():
    #    raise ValueError("Data Quality Check Failed: Invalid laps.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")

def dataQualityChecksFactLap(df):
    print(f"Fact_lap redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes) 
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe fact_lap is empty.")  

def dataQualityChecksFactPitstops(df):
    print(f"Fact_pitstops redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe fact_pitstops is empty.")
    
def dataQualityChecksRaceAndStandings(df1, df2, wins):
    if max(df1[wins].fillna(0).tolist())>len(df2["raceId"]):
        raise ValueError("Data Quality Check Failed: Invalid wins.")

def keysQualityCheck(foreign_key_rows, primary_key_rows):
    if foreign_key_rows!=primary_key_rows:
        raise ValueError("Data Quality Check Failed: Invalid join on primary keys.")
    
def dateQualityCheck(dt1, dt2):
    if dt1.max()>dt2.max():
         raise ValueError("Data Quality Check Failed: Invalid date of birth.")

def dqc_gold():
    dim_race = pd.read_sql('SELECT * FROM dim_race', engine)
    race_id_count=len(pd.read_sql('SELECT DISTINCT "raceId" from silver_layer', engine))
    dim_driver = pd.read_sql('SELECT * FROM dim_driver', engine)
    driver_id_count=len(pd.read_sql('SELECT DISTINCT "driverId" from silver_layer', engine))
    dim_status = pd.read_sql('SELECT * FROM dim_status', engine)
    status_id_count=len(pd.read_sql('SELECT DISTINCT "statusId" from silver_layer', engine))
    dim_constructor =pd.read_sql('SELECT * FROM dim_constructor', engine)
    constructor_id_count=len(pd.read_sql('SELECT DISTINCT "constructorId" from silver_layer', engine))
    dim_circuit = pd.read_sql('SELECT * FROM dim_circuit', engine)
    circuit_id_count=len(pd.read_sql('SELECT DISTINCT "circuitId" from silver_layer', engine))
    dim_driverstandings = pd.read_sql('SELECT * FROM dim_driverstandings', engine)
    driverstandings_id_count=len(pd.read_sql('SELECT DISTINCT "driverStandingsId" from silver_layer', engine))
    dim_constructorstandings = pd.read_sql('SELECT * FROM dim_constructorstandings', engine)
    constructorstendings_id_count=len(pd.read_sql('SELECT DISTINCT "constructorStandingsId" from silver_layer', engine))
    fact_results = pd.read_sql('SELECT * FROM fact_results', engine)
    result_id_count=len(pd.read_sql('SELECT DISTINCT "resultId" from silver_layer', engine))
    fact_lap = pd.read_sql('SELECT * FROM fact_lap', engine)
    fact_pitstops = pd.read_sql('SELECT * FROM fact_pitstops', engine)
    primary_dim_race=len(pd.read_sql('SELECT "raceId" from dim_race', engine))
    primary_dim_driver=len(pd.read_sql('SELECT "driverId" from dim_driver', engine))
    primary_dim_constructor=len(pd.read_sql('SELECT "constructorId" from dim_constructor', engine))
    primary_dim_circuit=len(pd.read_sql('SELECT "circuitId" from dim_circuit', engine))
    primary_dim_driverstandings=len(pd.read_sql('SELECT "driverStandingsId" from dim_driverstandings', engine))
    primary_dim_constructorstandings=len(pd.read_sql('SELECT "constructorStandingsId" from dim_constructorstandings', engine))
    primary_dim_status=len(pd.read_sql('SELECT "statusId" from dim_status', engine))
    foreign_fact_race=len(pd.read_sql('SELECT distinct "raceId" from fact_results', engine))
    foreign_fact_driver=len(pd.read_sql('SELECT distinct "driverId" from fact_results', engine))
    foreign_fact_constructor=len(pd.read_sql('SELECT distinct "constructorId" from fact_results', engine))
    foreign_fact_circuit=len(pd.read_sql('SELECT distinct "circuitId" from fact_results', engine))
    foreign_fact_driverstandings=len(pd.read_sql('SELECT distinct "driverStandingsId" from fact_results', engine))
    foreign_fact_constructorstandings=len(pd.read_sql('SELECT distinct "constructorStandingsId" from fact_results', engine))
    foreign_fact_status=len(pd.read_sql('SELECT distinct "statusId" from fact_results', engine))
    dataQualityChecksDim(dim_circuit, circuit_id_count)
    dataQualityChecksDim(dim_constructor, constructor_id_count)
    dataQualityChecksDim(dim_constructorstandings, constructorstendings_id_count)
    dataQualityChecksDim(dim_driver, driver_id_count)
    dataQualityChecksDim(dim_driverstandings, driverstandings_id_count)
    dataQualityChecksDim(dim_race, race_id_count)
    dataQualityChecksDim(dim_status, status_id_count)
    dataQualityChecksFactResults(fact_results, result_id_count)
    dataQualityChecksFactLap(fact_lap)
    dataQualityChecksFactPitstops(fact_pitstops)
    dataQualityChecksRaceAndStandings(dim_driverstandings, dim_race, 'driverstandings_wins')
    dataQualityChecksRaceAndStandings(dim_constructorstandings, dim_race, 'constructorstandings_wins')
    keysQualityCheck(foreign_fact_race, primary_dim_race)
    keysQualityCheck(foreign_fact_driver, primary_dim_driver)
    keysQualityCheck(foreign_fact_constructor, primary_dim_constructor)
    keysQualityCheck(foreign_fact_circuit, primary_dim_circuit)
    keysQualityCheck(foreign_fact_driverstandings, primary_dim_driverstandings)
    keysQualityCheck(foreign_fact_constructorstandings, primary_dim_constructorstandings)
    keysQualityCheck(foreign_fact_status, primary_dim_status)
    dateQualityCheck(dim_driver['dob'], dim_race['date'])

if __name__=='__main__':
    dqc_gold()