import pandas as pd

df = pd.read_csv("./voters/notfound.csv")
print(df.shape)


apt_df = df[df['Street address line 1 - Home'].astype(str).str.contains("Apt|apt|Unit|unit")]
print(type(df))
df_dict = apt_df.to_dict('records')
print(df_dict[0])
for l in df_dict:
    if "Apt" in l['Street address line 1 - Home']:
        l['old_address'] = l['Street address line 1 - Home']
        l['Street address line 1 - Home'] = l['Street address line 1 - Home'].split("Apt")[0]
    elif "apt" in l['Street address line 1 - Home']:
        l['old_address'] = l['Street address line 1 - Home']
        l['Street address line 1 - Home'] = l['Street address line 1 - Home'].split("apt")[0]
    elif "Unit" in l['Street address line 1 - Home']:
        l['old_address'] = l['Street address line 1 - Home']
        l['Street address line 1 - Home'] = l['Street address line 1 - Home'].split("Unit")[0] 
    elif "unit" in l['Street address line 1 - Home']:
        l['old_address'] = l['Street address line 1 - Home']
        l['Street address line 1 - Home'] = l['Street address line 1 - Home'].split("unit")[0]   
    else:
        l['old_address'] = l['Street address line 1 - Home']    

df = pd.DataFrame(df_dict)
df.to_csv("./voters/runnotfound.csv")            