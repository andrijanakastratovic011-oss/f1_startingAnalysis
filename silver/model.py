import sqlalchemy as db
import pandas as pd
import validators
from sqlalchemy.ext.declarative import declarative_base
import numpy as np

Base = declarative_base()

class Silver(Base):
    __tablename__="silver_layer"
    id=db.Column(db.Integer, primary_key=True)
    resultId=db.Column(db.Integer)
    raceId=db.Column(db.Integer)
    driverId=db.Column( db.Integer)
    constructorId=db.Column(db.Integer)
    number=db.Column(db.Integer)
    grid=db.Column(db.Integer)
    position=db.Column(db.Integer)
    positionText=db.Column(db.String(200))
    positionOrder=db.Column(db.Integer)
    points=db.Column(db.Float)
    laps=db.Column(db.Integer)
    milliseconds=db.Column(db.Integer)
    fastestLap=db.Column(db.Integer)
    rank=db.Column(db.Integer)
    fastestLapSpeed=db.Column(db.Float)
    statusId=db.Column(db.Integer)
    year=db.Column(db.Integer)
    round=db.Column(db.Integer)
    lat=db.Column(db.Float)
    lng=db.Column(db.Float)
    alt=db.Column(db.Float)
    drivers_number=db.Column( db.Integer)
    lap=db.Column(db.Integer)
    laptimes_position=db.Column(db.Integer)
    laptimes_milliseconds=db.Column(db.Integer)
    pitstops_lap=db.Column( db.Integer)
    pitstops_milliseconds=db.Column(db.Integer)
    stop=db.Column(db.Integer)
    driverStandingsId=db.Column(db.Integer)
    driverstandings_points=db.Column(db.Float)
    driverstandings_position=db.Column(db.Integer)
    driverstandings_wins=db.Column(db.Integer)
    constructorStandingsId=db.Column(db.Integer)
    constructorstandings_points=db.Column(db.Float)
    constructorstandings_position=db.Column(db.Integer)
    constructorstandings_wins=db.Column(db.Integer)
    constructors_name=db.Column(db.String(200))
    race_name=db.Column(db.String(200))
    circuit_name=db.Column(db.String(200))
    location=db.Column(db.String(200))
    country=db.Column(db.String(200))
    forename=db.Column(db.String(200))
    surname= db.Column(db.String(200))
    driver_nationality=db.Column(db.String(200))
    constructors_nationality=db.Column(db.String(200))
    constructorstandings_positionText=db.Column(db.String(200))
    driverstandings_positionText=db.Column(db.String(200))
    status=db.Column(db.String(200))
    duration=db.Column(db.Float)
    date=db.Column( db.Date)
    quali_date=db.Column( db.Date)
    dob=db.Column(db.Date)
    sprint_date=db.Column(db.Date)
    time=db.Column(db.String(200))
    fastestLapTime=db.Column(db.String(200))
    races_time=db.Column(db.String(200))
    quali_time=db.Column(db.String(200))
    sprint_time=db.Column( db.String(200))
    laptimes_time=db.Column( db.String(200))
    pitstops_time=db.Column(db.String(200))
    race_url=db.Column(db.String(200))
    circuit_url=db.Column(db.String(200))
    constructors_url=db.Column(db.String(200))
    driver_url=db.Column(db.String(200))
    circuitRef=db.Column(db.String(200))
    driverRef=db.Column(db.String(200))
    constructorRef=db.Column(db.String(200))
    code=db.Column(db.String(200))
    circuitId=db.Column(db.Integer)
    fp1_date=db.Column(db.Date)
    fp2_date=db.Column(db.Date)
    fp3_date=db.Column(db.Date)
    fp1_time=db.Column(db.String(200))
    fp2_time=db.Column(db.String(200))
    fp3_time=db.Column(db.String(200))

class DataCleaner:
    def __init__(self, df: pd.DataFrame, name: str="dataset"):
        df_copy=df.copy()
        self.df=df_copy
        self.name=name

    def fix_nulls(self, columns: list):
        self.df[columns] = self.df[columns].replace('\\N', np.nan)
        return self


    def standardize_text_columns(self, columns: list):
        for column in columns:
            self.df[column]=self.df[column].astype(str)
            self.df[column]=self.df[column].str.strip()
        return self

    def fix_dates (self, columns: list):
        for column in columns:
            self.df[column]=pd.to_datetime(self.df[column], dayfirst=True, errors='coerce', format='mixed')
        return self
 
    def standardize_numeric(self, columns: list):
        for column in columns:
            self.df[column]=pd.to_numeric(self.df[column], errors='coerce')
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

