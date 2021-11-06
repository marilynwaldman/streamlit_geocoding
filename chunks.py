import os
import pandas as pd 
import os.path
from pathlib import Path
import sys
import shutil

def get_chunks(indir):
    print(indir)
    
    df = pd.read_csv('./voters.csv', header=0,
                 low_memory=False,
                 dtype=str)
    n = 10  #chunk row size
    list_df = [df[i:i+n] for i in range(0,df.shape[0],n)]
    for index, file in enumerate(list_df):
         
         filename =  indir + "/file_" + str(index) + '.csv'
         file.to_csv(filename) # relative position
         

    return



def get_dir():
    filename="voters.csv"
    split_names = filename.split(".")
    print(len(split_names))
    print(split_names)
    dir = "./"
    if len(split_names) > 1:
         print("here")
         dir = dir + split_names[0]
    else:
         dir = dir + filename
    return dir     

def remove_directory(dir):
    try:
       shutil.rmtree(dir)
    except OSError as e:
       print("Message: %s - %s." % (e.filename, e.strerror)) 
    return 


def remove_directories(dir,indir, outdir, current_file, bad_files):
    #delete directories if they exist
    remove_directory(indir)
    remove_directory(outdir)
    remove_directory(current_file)
    remove_directory(bad_files)
    

    return
def create_directories(dir,indir, outdir, current_file, bad_files):
    # create directories
    Path(indir).mkdir(parents=True, exist_ok=True)
    Path(outdir).mkdir(parents=True, exist_ok=True)
    Path(current_file).mkdir(parents=True, exist_ok=True)
    Path(bad_files).mkdir(parents=True, exist_ok=True)
    

    return

    
def main():
    dir = get_dir()
    indir = dir + "/input"
    outdir = dir + "/output"
    current_file = dir + "/current"
    bad_files = dir + "/badfiles"
    
    remove_directories(dir, indir, outdir, current_file, bad_files)
    create_directories(dir, indir, outdir, current_file, bad_files)

    chunks = get_chunks(indir)
    #df = process_chunks()


if __name__ == "__main__":
    main()