import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
f1_df=pd.read_csv('dataEngineeringDataset.csv')

class DataCleaner:
    def __init__(self, df: pd.DataFrame, name: str="dataset"):
        df_copy=df.copy()
        self.df=df
        self.name=name

    def standardize_text_columns(self, columns: list):
        for column in columns:
            self.df[column]=self.df[column].astype(str)
            self.df[column]=self.df[column].str.strip()
            self.df[column]=self.df[column].str.capitalize()
        return self

    def fix_dates (self, columns: list):
        for column in columns:
            self.df[column]=pd.to_datetime(self.df[column], dayfirst=True, errors='coerce', format='mixed')
        return self

    def fix_nulls(self, columns: list):
        for column in columns:
            if (self.df[column].str=='\\N'):
                self.df[column]=pd.NA
        return self
    
    def fill_nulls(self, strategy: dict):
        for key, value in strategy.items():
           self.df[key]=self.df[key].fillna(value)
        return self
 
    def standardize_numeric(self, columns: list):
        for column in columns:
            self.df[column]=pd.to_numeric(self.df[column], errors='coerce')
        return self
    
    def standardize_time_columns(self, columns: list):
        for column in columns:
            self.df[column]=pd.to_datetime(self.df[column], format='%I:%M:%S %p', errors='coerce')
        return self

    def standardize_interval_columns(self, columns: list):
        for column in columns:
            self.df[column]=pd.to_timedelta(self.df[column], errors='coerce')
        return self
    
    def fix_upper(self, column: str):
        self.df[column]=self.df[column].str.upper()
        return self
    
    def fix_lower(self, columns: list):
        for column in columns:
            self.df[column]=self.df[column].str.lower()
        return self
 
    def standardize_urls(self, columns: list):
        for column in columns:
            self.df[column]=self.df[column].where(self.df[column].str.match(r'https?://\S+'), other='Invalid url')
        return self
    



if __name__=="__main__":
    load_dotenv()
    engine=create_engine(os.getenv('DATABASE_URL'))
    bronze_row=pd.read_csv('dataEngineeringDataset.csv', low_memory=False)
    bronze_row.to_sql("bronze_row", engine, if_exists='replace', index=False)
    bronze_from_db = pd.read_sql('SELECT * FROM bronze_row', engine)
    silver = DataCleaner(bronze_from_db, 'silver_row')
    silver_row=(silver.standardize_text_columns(['positionText', 'name_x', 'name_y', 'location', 'country', 'forename', 'surname', 'nationality', 'nationality_constructors', 'positionText_constructorstandings', 'status']).fix_dates(['date', 'quali_date', 'dob', 'sprint_date']).standardize_time_columns(['time', 'fastestLapTime','time_races','quali_time', 'sprint_time', 'time_laptimes', 'time_pitstops']).standardize_numeric(['resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'position', 'positionOrder', 'points', 'laps', 'milliseconds', 'fastestLap', 'rank', 'fastestLapSpeed', 'statusId', 'year', 'round', 'lat', 'lng', 'alt', 'number_drivers', 'lap', 'position_laptimes', 'milliseconds_laptimes', 'lap_pitstops', 'milliseconds_pitstops', 'stop', 'driverStandingsId', 'points_driverstandings', 'position_driverstandings', 'wins', 'constructorStandingsId', 'points_constructorstandings', 'position_constructorstandings', 'wins_constructorstandings']).standardize_interval_columns(['duration']).standardize_urls(['url_x', 'url_y', 'url', 'url_constructors']).fix_lower(['circuitRef', 'driverRef', 'constructorRef']).fix_upper('code'))
    silver_row.df.to_csv("silver.csv", index=False)