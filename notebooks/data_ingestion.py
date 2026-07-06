import pandas as pd
# import os

# # files = os.listdir("data/raw")

# # for file in files:
# #     if file.endswith(".csv"):
# #         path = os.path.join("data/raw",file)

# #         df = pd.read_csv(path)
# #         print("="*100)
# #         print(file)
# #         print("="*100)

# #         print("Shape : ",df.shape)
# #         print("-"*50)
# #         print("Data types : \n",df.dtypes)
# #         print("-"*50)
# #         print("First five recs : \n",df.head())
# #         print("-"*50)

# fund_master = pd.read_csv("data/raw/01_fund_master.csv")
# # print(fund_master.columns.tolist())

# # cols = ["fund_house","category","sub_category","risk_category"]

# # for col in cols:
# #     print("="*50)
# #     print(f"Unique {col} :")
# #     print(fund_master[col].unique())

# nav_history = pd.read_csv("data/raw/02_nav_history.csv")
# # print(nav_history.columns.to_list())

# fund_amfi_codes = set(fund_master["amfi_code"])
# nav_amfi_codes = set(nav_history["amfi_code"])

# missing_codes = fund_amfi_codes.difference(nav_amfi_codes)

# if len(missing_codes) == 0:
#     print("All AMFI codes from fund_master exist in nav_history")
# else:
#     print("Missing codes : \n",missing_codes)


# files = [
#     "nav_history_cleaned.csv",
#     "fund_scorecard.csv",
#     "scheme_performance_cleaned.csv",
#     "aum_by_fund_house_cleaned.csv",
#     "benchmark_indices_cleaned.csv",
#     # "dim_date.csv"
#     "fund_master_cleaned.csv"
# ]

# for file in files:
#     df = pd.read_csv(f"data/processed/{file}")
#     print(f"\n===== {file} =====")
#     print(df.columns.tolist())

# ===========================
# Read CSV files
# ===========================
nav = pd.read_csv("data/processed/nav_history_cleaned.csv")
fund = pd.read_csv("data/processed/fund_master_cleaned.csv")
performance = pd.read_csv("data/processed/scheme_performance_cleaned.csv")
scorecard = pd.read_csv("data/processed/fund_scorecard.csv")
aum = pd.read_csv("data/processed/aum_by_fund_house_cleaned.csv")
benchmark = pd.read_csv("data/processed/benchmark_indices_cleaned.csv")

# ===========================
# Convert dates
# ===========================
nav["date"] = pd.to_datetime(nav["date"])
aum["date"] = pd.to_datetime(aum["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

# ===========================
# Merge NAV + Fund Master
# ===========================
master = nav.merge(fund, on="amfi_code", how="left")

# ===========================
# Merge Scheme Performance
# ===========================
master = master.merge(performance.drop(columns=["scheme_name"], errors="ignore"), on="amfi_code", how="left")

# ===========================
# Merge Fund Scorecard
# ===========================
master = master.merge(scorecard[
        [
            "amfi_code",
            "Fund_Score",
            "CAGR_3Y",
            "Sharpe_Ratio",
            "Alpha",
            "Max_Drawdown"
        ]
    ], on="amfi_code", how="left")

# ===========================
# Merge Benchmark Values
# benchmark = index_name
# ===========================
master = master.merge(benchmark, left_on=["benchmark", "date"], right_on=["index_name", "date"], how="left")
print(master.columns.tolist())
master.rename(columns={
    "fund_house_x": "fund_house",
    "category_x": "category",
    "plan_x": "plan",
    "expense_ratio_pct_x": "expense_ratio_pct"
}, inplace=True)

master.drop(columns=[
    "fund_house_y",
    "category_y",
    "plan_y",
    "expense_ratio_pct_y"
], inplace=True)
# ===========================
# Merge Fund House AUM
# ===========================
master = master.merge(
    aum[
        [
            "date",
            "fund_house",
            "aum_lakh_crore",
            "aum_crore",
            "num_schemes"
        ]
    ],
    on=["date", "fund_house"],
    how="left"
)

# ===========================
# Remove duplicate columns
# ===========================
master = master.loc[:, ~master.columns.duplicated()]

# ===========================
# Sort
# ===========================
master = master.sort_values(
    ["scheme_name", "date"]
)

# ===========================
# Save
# ===========================
master.to_csv("master_dashboard.csv", index=False)

print("="*50)
print("Master Dashboard Dataset Created Successfully!")
print("="*50)

print(master.head())
print(master.shape)
print(master[["scheme_name", "benchmark", "index_name", "close_value"]].head())
print("\nRows :", len(master))
print("Columns :", len(master.columns))