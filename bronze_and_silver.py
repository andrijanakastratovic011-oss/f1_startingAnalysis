import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import validators

f1_df=pd.read_csv('dataEngineeringDataset.csv')

class DataCleaner:
    def __init__(self, df: pd.DataFrame, name: str="dataset"):
        df_copy=df.copy()
        self.df=df_copy
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
 
    def standardize_numeric(self, columns: list):
        for column in columns:
            self.df[column]=pd.to_numeric(self.df[column], errors='coerce')
        return self
    
    def standardize_time_columns(self, columns: list):
        for column in columns:
            dt=self.df[column]=pd.to_datetime(self.df[column], format='%I:%M:%S %p', errors='coerce')
            self.df[column]=dt.dt.strftime("%H:%M:%S")
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
            self.df[column] = self.df[column].astype(str).str.strip()
            self.df[column]=self.df[column].apply(lambda x: x if validators.url(x) is True else pd.NA)
        return self



if __name__=="__main__":
    load_dotenv()
    engine=create_engine(os.getenv('DATABASE_URL'))
    bronze_layer=pd.read_csv('dataEngineeringDataset.csv', low_memory=False)
    bronze_layer.to_sql("bronze_layer", engine, if_exists='replace', index=False)
    bronze_from_db = pd.read_sql('SELECT * FROM bronze_layer', engine)
    silver = DataCleaner(bronze_from_db, 'silver_layer')
    silver_layer=(silver.standardize_text_columns(['positionText', 'name_x', 'name_y', 'location', 'country', 'forename', 'surname', 'nationality', 'nationality_constructors', 'positionText_constructorstandings', 'status']).fix_dates(['date', 'quali_date', 'dob', 'sprint_date']).standardize_time_columns(['time', 'fastestLapTime','time_races','quali_time', 'sprint_time', 'time_laptimes', 'time_pitstops']).standardize_numeric(['resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'position', 'positionOrder', 'points', 'laps', 'milliseconds', 'fastestLap', 'rank', 'fastestLapSpeed', 'statusId', 'year', 'round', 'lat', 'lng', 'alt', 'number_drivers', 'lap', 'position_laptimes', 'milliseconds_laptimes', 'lap_pitstops', 'milliseconds_pitstops', 'stop', 'driverStandingsId', 'points_driverstandings', 'position_driverstandings', 'wins', 'constructorStandingsId', 'points_constructorstandings', 'position_constructorstandings', 'wins_constructorstandings', 'duration']).standardize_urls(['url_x', 'url_y', 'url', 'url_constructors']).fix_lower(['circuitRef', 'driverRef', 'constructorRef']).fix_upper('code'))
    silver_layer.df.to_sql("silver_layer", engine, if_exists='replace', index=False)
    silver_layer.df.to_csv("silver.csv", index=False)
    rows_bronze, columns_bronze=bronze_layer.shape
    rows_silver, columns_silver=silver_layer.df.shape
    print(f"Bronze layer: {rows_bronze} {columns_bronze}, silver layer: {rows_silver} {columns_silver}")
    print(f"Bronze layer- distinct resultId: {bronze_layer['resultId'].nunique()}")
    print(f"Silver layer- distinct resultId: {silver_layer.df['resultId'].nunique()}")
    print(f"Bronze layer- distinct raceId: {bronze_layer['raceId'].nunique()}")
    print(f"Silver layer- distinct raceId: {silver_layer.df['raceId'].nunique()}")
    print(f"Bronze layer- distinct driverId: {bronze_layer['driverId'].nunique()}")
    print(f"Silver layer- distinct driverId: {silver_layer.df['driverId'].nunique()}")
    print(f"Bronze_layer- nulls: {bronze_layer.isnull().sum()}")
    print(f"Silver_layer- nulls: {silver_layer.df.isnull().sum()}")