from load import load_dim_circuit, load_dim_constructor, load_dim_constructorstandings, load_dim_driver, load_dim_driverstandings, load_dim_race, load_dim_status, load_fact_results, load_fact_lap, load_fact_pitstops
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))
dim_race = load_dim_race(engine)
def DataQualityChecksRace():
    print(f"Dim_race redovi: {len(dim_race)}")
    print("Null vrijednosti po kolonama:")
    print(dim_race.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(dim_race.dtypes)

dim_driver = load_dim_driver(engine)
def DataQualityChecksDriver():
    print(f"Dim_driver redovi: {len(dim_driver)}")
    print("Null vrijednosti po kolonama:")
    print(dim_driver.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(dim_driver.dtypes)

dim_status = load_dim_status(engine)
def DataQualityChecksStatus():
    print(f"Dim_status redovi: {len(dim_status)}")
    print("Null vrijednosti po kolonama:")
    print(dim_status.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(dim_status.dtypes)

dim_constructor = load_dim_constructor(engine)
def DataQualityChecksConstructor():
    print(f"Dim_constructor redovi: {len(dim_constructor)}")
    print("Null vrijednosti po kolonama:")
    print(dim_constructor.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(dim_constructor.dtypes)

dim_circuit = load_dim_circuit(engine)
def DataQualityChecksCircuit():
    print(f"Dim_circuit redovi: {len(dim_circuit)}")
    print("Null vrijednosti po kolonama:")
    print(dim_circuit.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(dim_circuit.dtypes)
          
dim_driverstandings = load_dim_driverstandings(engine)
def DataQualityChecksDriverStandings():
    print(f"Dim_driverStandings redovi: {len(dim_driverstandings)}")
    print("Null vrijednosti po kolonama:")
    print(dim_driverstandings.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(dim_driverstandings.dtypes)

dim_constructorstandings = load_dim_constructorstandings(engine)
def DataQualityChecksConstructorStandings():
    print(f"Dim_constructorStandings redovi: {len(dim_constructorstandings)}")
    print("Null vrijednosti po kolonama:")
    print(dim_constructorstandings.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(dim_constructorstandings.dtypes)

fact_results = load_fact_results(engine)
def DataQualityChecksFactResults():
    print(f"Fact redovi: {len(fact_results)}")
    print("Null vrijednosti po kolonama:")
    print(fact_results.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(fact_results.dtypes)

fact_lap = load_fact_lap(engine)
def DataQualityChecksFactLap():
    print(f"Fact_lap redovi: {len(fact_lap)}")
    print("Null vrijednosti po kolonama:")
    print(fact_lap.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(fact_lap.dtypes)   

fact_pitstops = load_fact_pitstops(engine)
def DataQualityChecksFactPitstops():
    print(f"Fact_pitstops redovi: {len(fact_pitstops)}")
    print("Null vrijednosti po kolonama:")
    print(fact_pitstops.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(fact_pitstops.dtypes)

DataQualityChecksCircuit()
DataQualityChecksCircuit()
DataQualityChecksConstructorStandings()
DataQualityChecksDriver()
DataQualityChecksDriverStandings()
DataQualityChecksRace()
DataQualityChecksStatus()
DataQualityChecksFactResults()
DataQualityChecksFactLap()
DataQualityChecksFactPitstops()