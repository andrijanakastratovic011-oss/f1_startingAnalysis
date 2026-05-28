import pandas as pd
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
    # BRONZE - samo učitaj i sačuvaj sirove podatke 
    bronze_row = pd.read_csv("dataEngineeringDataset.csv")
    bronze_row.to_csv("bronze.csv", index=False)
    # SILVER - učitaj bronze i primijeni čišćenje
    silver = DataCleaner(pd.read_csv("bronze.csv"), "silver")
    strategy={'position': '0',
              'fastestLap': '0',
              'number_drivers': '0',
              'milliseconds': '0'}
    silver = (silver.fix_nulls(['position', 'fastestLap', 'number_drivers', 'milliseconds']).fill_nulls(strategy).standardize_text_columns(['positionText', 'name_x', 'name_y', 'location', 'country', 'forename', 'surname', 'nationality', 'nationality_constructors', 'status', 'positionText_driverstandings', 'positionText_constructorstandings']).fix_dates(['date', 'fp1_date', 'fp2_date', 'fp3_date', 'quali_date', 'sprint_date', 'dob']) .standardize_numeric(['position', 'milliseconds', 'fastestLap', 'number_drivers', 'resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'positionOrder', 'laps', 'rank', 'statusId', 'year', 'round', 'circuitId', 'lap', 'position_laptimes', 'milliseconds_laptimes', 'stop', 'lap_pitstops', 'milliseconds_pitstops', 'driverStandingsId', 'position_driverstandings', 'wins', 'constructorStandingsId', 'position_constructorstandings', 'wins_constructorstandings', 'points', 'lat', 'lng', 'alt', 'points_driverstandings', 'points_constructorstandings', 'fastestLapSpeed']).standardize_urls(['url', 'url_x', 'url_y', 'url_constructors']).standardize_time_columns(['time', 'fastestLapTime', 'time_races', 'fp1_time', 'fp2_time', 'fp3_time', 'quali_time', 'sprint_time', 'time_laptimes', 'time_pitstops']).standardize_interval_columns(['duration']).fix_lower(['driverRef', 'constructorRef', 'circuitRef']).fix_upper('code'))
    silver.df.to_csv("silver.csv", index=False)

    from sqlalchemy import create_engine
    engine=create_engine("postgresql://postgres:12345678@host:5432/postgres")
    bronze_row.to_sql("bronze_row", engine, if_exists="replace", index=False)
    silver = pd.read_sql("SELECT * FROM bronze_row", engine)