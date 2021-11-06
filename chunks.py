import os
import pandas as pd 

def get_chunks():
    
    filename="voters.csv"
    split_names = filename.split(".")
    inputdir = split_names[;]
    df = pd.read_csv('./voters.csv', header=0,
                 low_memory=False,
                 dtype=str)
    n = 50  #chunk row size
    list_df = [df[i:i+n] for i in range(0,df.shape[0],n)]
    for index, chunkdf in enumerate(list_df):
         
         filename =  './inputchunk/input' + str(index) + '.csv'
         print(filename)
         chunkdf.to_csv(filename) # relative position
         df2 = pd.read_csv(filename)

    return

def process_df(df):

    print("new df")
    print(df)
    return

def process_chunks():
    dir = "./inputchunk" # Your directory
    for x in os.listdir(dir):
        filename = dir + "/" +  x
        df_chunk = pd.read_csv(filename)
        process_df(df_chunk)
       


def main():
    chunks = get_chunks()
    df = process_chunks()


if __name__ == "__main__":
    main()