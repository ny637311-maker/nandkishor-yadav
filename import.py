import pandas as pd

df =pd.read_csv(r"c:\Users\ny637\Downloads\student.csv - Sheet1.csv")
print(df.head())
print(df.info())
print(df.describe())