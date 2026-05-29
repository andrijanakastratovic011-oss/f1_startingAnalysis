from model import Base, DataCleaner
import pandas as pd
from sqlalchemy import create_engine, text

def load_silver(engine):
    Base.metadata.create_all(engine)

    bronze_df = pd.read_sql("SELECT * FROM bronze_layer", engine)

    silver = DataCleaner(bronze_df, "silver_layer")
    silver_layer=(silver.standardize_text_columns(['positionText', 'name_x', 'name_y', 'location', 'country', 'forename', 'surname', 'nationality', 'nationality_constructors', 'positionText_constructorstandings', 'status', 'time', 'fastestLapTime','time_races','quali_time', 'sprint_time', 'time_laptimes', 'time_pitstops']).standardize_numeric(['resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'position', 'positionOrder', 'points', 'laps', 'milliseconds', 'fastestLap', 'rank', 'fastestLapSpeed', 'statusId', 'year', 'round', 'lat', 'lng', 'alt', 'number_drivers', 'lap', 'position_laptimes', 'milliseconds_laptimes', 'lap_pitstops', 'milliseconds_pitstops', 'stop', 'driverStandingsId', 'points_driverstandings', 'position_driverstandings', 'wins', 'constructorStandingsId', 'points_constructorstandings', 'position_constructorstandings', 'wins_constructorstandings', 'duration']).standardize_urls(['url_x', 'url_y', 'url', 'url_constructors']).fix_lower(['circuitRef', 'driverRef', 'constructorRef']).fix_upper('code').fix_dates(['date', 'fp1_date', 'fp2_date', 'fp3_date', 'quali_date', 'sprint_date', 'dob']))
    silver_layer.df=silver_layer.df.rename(columns={"name_x":"name_race", "url_x":"url_race", "name_y":"name_circuit", "url_y":"url_circuit", "name":"name_constructors", "url":"url_driver"})
    with engine.connect() as connection:
        connection.execute(text("TRUNCATE TABLE silver_layer"))
        connection.commit()
    silver_layer.df.to_sql("silver_layer", engine, if_exists='replace', index=False)
    return silver_layer.df