import pandas as pd
import os

# files = os.listdir("data/raw")

# for file in files:
#     if file.endswith(".csv"):
#         path = os.path.join("data/raw",file)

#         df = pd.read_csv(path)
#         print("="*100)
#         print(file)
#         print("="*100)

#         print("Shape : ",df.shape)
#         print("-"*50)
#         print("Data types : \n",df.dtypes)
#         print("-"*50)
#         print("First five recs : \n",df.head())
#         print("-"*50)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
# print(fund_master.columns.tolist())

# cols = ["fund_house","category","sub_category","risk_category"]

# for col in cols:
#     print("="*50)
#     print(f"Unique {col} :")
#     print(fund_master[col].unique())

nav_history = pd.read_csv("data/raw/02_nav_history.csv")
# print(nav_history.columns.to_list())

fund_amfi_codes = set(fund_master["amfi_code"])
nav_amfi_codes = set(nav_history["amfi_code"])

missing_codes = fund_amfi_codes.difference(nav_amfi_codes)

if len(missing_codes) == 0:
    print("All AMFI codes from fund_master exist in nav_history")
else:
    print("Missing codes : \n",missing_codes)


