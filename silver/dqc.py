import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def dqc_silver():
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    df = pd.read_sql('SELECT * FROM silver_layer', engine)
    br=pd.read_sql('select * from bronze_layer', engine)
    print(f"Silver redovi: {len(df)}")
    if len(df)!=len(br):
        raise ValueError("Data Quality Check Failf: Some rows are lost.")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)
    if df.empty:
        raise ValueError("Data Quality Check Failed: The dataframe is empty.")
    if df.astype(str).eq('\\N').any().any():
        raise ValueError("Data Quality Check Failed: There is '\\N' in dataframe.")
    if ((df['year']>2023) | (df['year']<2012)).any():
        raise ValueError("Data Quality Check Failed: Invalid year.")
    point=['points', 'points_driverstandings', 'points_constructorstandings']
    for p in point:
        if (df[p]<0).any():
            raise ValueError("Data Quality Check Failed: Invalid points.")
    position=['position', 'position_driverstandings', 'position_constructorstandings']
    for po in position:
        if (df[po]<0).any():
            raise ValueError("Data Quality Check Failed: Invalid position.")
    if (df['grid']).any()<0:
        raise ValueError("Data Quality Check Failed: Invalid grid.")

if __name__=='__main__':
    dqc_silver()
