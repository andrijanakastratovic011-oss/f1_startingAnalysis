import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dataset=pd.read_csv('dataEngineeringDataset.csv')
dataset.info()
print(dataset.isnull().sum())
print(dataset.describe())
print(dataset.duplicated())
for col in dataset.select_dtypes(include='object').columns:
    print(f"\n--- {col} ---")
    print(dataset[col].unique())

