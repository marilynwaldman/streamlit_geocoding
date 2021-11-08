import pandas as pd
import os
from os import path

df = pd.read_csv("./voters/found.csv")
print(df.head(6))
print(df.columns)

outdf = df[['Precinct','Latitude', 'Longitude','City - Home', 'State/Province - Home', 'Zip/Postal Code - Home',]]
outdf.to_csv("./voters/afew.csv")      
