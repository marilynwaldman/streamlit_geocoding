import pandas as pd
import os
from os import path

def get_dir(filename):
    
    split_names = filename.split(".")
    
    dir = "."
    if len(split_names) > 1:
         dir = dir + split_names[-2]
    else:
         dir = dir + filename
    return dir 
    
def append_files(dir):

    count = 0
    print(dir)

    for file in os.listdir(dir):

        if not file.endswith ('.csv'):
                continue

        readpath = dir + "/" + file
        df_chunk = pd.read_csv(readpath)
        df_chunk['chunkfile'] = file
        #create master
        if count == 0:
            master_df = df_chunk
            print(master_df)
        else:
            master_df = master_df.append(df_chunk)  
        count = count + 1      
        

    return master_df  

def get_found(out_df):
        found_df = out_df[(out_df.Location_found == "found")] 
        #not_found_df = out_df['Location_found'].isnull().values
        
    
        not_found_df = out_df[out_df['Latitude'].isnull() | \
                               out_df['Longitude'].isnull()]
        return found_df, not_found_df

def main():
    filename="./voters/runnotfound.csv"
    dir = get_dir(filename)
    print(dir)
    outdir = dir + "/output"
    current_dir = dir + "/current"
    print(outdir)

    geocoded_csv = dir + "/" + "geocoded.csv"
    found_csv = dir + "/" + "found.csv"
    not_found_csv = dir + "/" + "notfound.csv"
    out_df = append_files(outdir)
    out_df.to_csv(geocoded_csv)
    found_df, not_found_df = get_found(out_df)
    found_df.to_csv(found_csv)
    not_found_df.to_csv(not_found_csv)
    bad_files_csv = dir + "/" + "didnotgeocode.csv"
    bad_files_df = append_files(current_dir)
    bad_files_df.to_csv(bad_files_csv)

    return

if __name__ == "__main__":
    main()
count = 0

