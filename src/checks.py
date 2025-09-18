import pandas as pd

def check_missing(df):
    return df.isnull().sum().to_dict()

def check_duplicates(df):
    return {"duplicate_rows": df.duplicated().sum()}
