import pandas as pd
import os

files = os.listdir("data/raw")

for file in files:
    if file.endswith(".csv"):
        path = os.path.join("data/raw",file)

        df = pd.read_csv(path)
        print("="*100)
        print(file)
        print("="*100)

        print("Shape : ",df.shape)
        print("-"*50)
        print("Data types : \n",df.dtypes)
        print("-"*50)
        print("First five recs : \n",df.head())
        print("-"*50)
