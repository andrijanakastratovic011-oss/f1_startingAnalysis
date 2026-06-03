from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

def DataQualityChecksRace(df, id):
    print(f"Dim_race redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe dim_race is empty.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")

def DataQualityChecksDriver(df, id):
    print(f"Dim_driver redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe dim_driver is empty.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")

def DataQualityChecksStatus(df, id):
    print(f"Dim_status redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe dim_status is empty.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")

def DataQualityChecksConstructor(df, id):
    print(f"Dim_constructor redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe dim_constructor is empty.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")

def DataQualityChecksCircuit(df, id):
    print(f"Dim_circuit redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe dim_circuit is empty.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")
          
def DataQualityChecksDriverStandings(df, id):
    print(f"Dim_driverStandings redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe dim_driverstandings is empty.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")

def DataQualityChecksConstructorStandings(df, id):
    print(f"Dim_constructorStandings redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe dim_constructorstandings is empty.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")

def DataQualityChecksFactResults(df, id):
    print(f"Fact redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe fact_result is empty.")
    if (df['fastestLap']>df['laps']).any():
        raise ValueError("Data Quality Check Failed: Invalid laps.")
    if id!=len(df):
        raise ValueError("Data Quality Check Failed: Some rows are lost.")

def DataQualityChecksFactLap(df):
    print(f"Fact_lap redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes) 
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe fact_lap is empty.")  

def DataQualityChecksFactPitstops(df):
    print(f"Fact_pitstops redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe fact_pitstops is empty.")
    
def DataQualityChecksRaceAndStandings(df1, df2, wins):
    if df1[wins].sum()>df2['raceId'].count():
        raise ValueError("Data Quality Check Failed: Invalid wins.")

def dqc_gold():
    dim_race = pd.read_sql('SELECT * FROM dim_race', engine)
    race_id_count=pd.read_sql('SELECT DISTINCT raceId from bronze_layer', engine)
    dim_driver = pd.read_sql('SELECT * FROM dim_driver', engine)
    driver_id_count=pd.read_sql('SELECT DISTINCT driverId from bronze_layer', engine)
    dim_status = pd.read_sql('SELECT * FROM dim_status', engine)
    status_id_count=pd.read_sql('SELECT DISTINCT statusId from bronze_layer', engine)
    dim_constructor =pd.read_sql('SELECT * FROM dim_constructor', engine)
    constructor_id_count=pd.read_sql('SELECT DISTINCT constructorId from bronze_layer', engine)
    dim_circuit = pd.read_sql('SELECT * FROM dim_circuit', engine)
    circuit_id_count=pd.read_sql('SELECT DISTINCT circuitId from bronze_layer', engine)
    dim_driverstandings = pd.read_sql('SELECT * FROM dim_driverstandings', engine)
    driverstandings_id_count=pd.read_sql('SELECT DISTINCT driverStandingsId from bronze_layer', engine)
    dim_constructorstandings = pd.read_sql('SELECT * FROM dim_constructorstandings', engine)
    constructorstendings_id_count=pd.read_sql('SELECT DISTINCT constructorStandingsId from bronze_layer', engine)
    fact_results = pd.read_sql('SELECT * FROM fact_results', engine)
    result_id_count=pd.read_sql('SELECT DISTINCT resultId from bronze_layer', engine)
    fact_lap = pd.read_sql('SELECT * FROM fact_lap', engine)
    fact_pitstops = pd.read_sql('SELECT * FROM fact_pitstops', engine)
    DataQualityChecksCircuit(dim_circuit, circuit_id_count)
    DataQualityChecksConstructor(dim_constructor, constructor_id_count)
    DataQualityChecksConstructorStandings(dim_constructorstandings, constructorstendings_id_count)
    DataQualityChecksDriver(dim_driver, driver_id_count)
    DataQualityChecksDriverStandings(dim_driverstandings, driverstandings_id_count)
    DataQualityChecksRace(dim_race, race_id_count)
    DataQualityChecksStatus(dim_status, status_id_count)
    DataQualityChecksFactResults(fact_results, result_id_count)
    DataQualityChecksFactLap(fact_lap)
    DataQualityChecksFactPitstops(fact_pitstops)
    DataQualityChecksRaceAndStandings(dim_driverstandings, dim_race, 'wins')
    DataQualityChecksRaceAndStandings(dim_constructorstandings, dim_race, 'wins_constructorstandings')

if __name__=='__main__':
    dqc_gold()