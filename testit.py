import pandas as pd
#df = pd.read_csv("./voters/runnotfound.csv")
df = pd.read_csv("./voters/notfound.csv")
print(df.columns)
#print(df[['Street address line 1 - Home','Zip/Postal Code - Home']].head()
print(df['Zip/Postal Code - Home'].astype(int).astype('string'))