import pandas as pd
from pandas.api.types import is_datetime64_any_dtype,is_numeric_dtype

def inspect_dataset(df):
    print("\n========== DATASET INFO ==========")
    df.info()
    print()
    print("Dataset Shape:", df.shape)
    print("\nNull values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

    print("\nUnique values in categorical columns:")

    for col in df.select_dtypes(include=["object", "string"]).columns:

        unique_values = df[col].unique()

        print(f"\n{col} ({len(unique_values)} unique values):")

        if len(unique_values) <= 20:
            print(unique_values)
        else:
            print(unique_values[:20])
            print("...")


def parse_date(df, column):
    df[column] = pd.to_datetime(df[column])

    if is_datetime64_any_dtype(df[column]):
        print(f"The {column} column successfully parsed to datetime!")
    else:
        print(f"Failed to parse {column} to datetime!")

    return df


def save_processed(df, filename):
    df.to_csv(f"data/processed/{filename}", index=False)
    print("Cleaned dataset saved successfully!")


def clean_nav_history():
    nav_history = pd.read_csv("data/raw/02_nav_history.csv")
    inspect_dataset(nav_history)

    nav_history = parse_date(nav_history, "date")

    nav_history = nav_history.sort_values(["amfi_code", "date"])
    print("Data sorted according to AMFI codes and Date successfully!")

    invalid_nav = nav_history[nav_history["nav"] <= 0]

    if len(invalid_nav) == 0:
        print("All NAV values are greater than 0")
    else:
        print("Invalid NAV records found:\n", invalid_nav)

    save_processed(nav_history, "nav_history_cleaned.csv")


def clean_investor_transactions():
    inv_transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
    inspect_dataset(inv_transactions)

    inv_transactions = parse_date(inv_transactions,"transaction_date")

    print("Unique KYC status values:\n",inv_transactions["kyc_status"].unique())

    amount = inv_transactions[inv_transactions["amount_inr"] <= 0]

    if len(amount) == 0:
        print("All transaction amounts are greater than 0")
    else:
        print("Invalid amounts found:\n", amount)

    save_processed(inv_transactions,"transactions_cleaned.csv")

def clean_scheme_performance():
    scheme_performance = pd.read_csv("data/raw/07_scheme_performance.csv")
    inspect_dataset(scheme_performance)

    return_yr = scheme_performance[["return_1yr_pct","return_3yr_pct","return_5yr_pct"]]

    for col in return_yr:

        if is_numeric_dtype(scheme_performance[col]):
            print(f"{col} is numeric.")
        else:
            print(f"{col} is NOT numeric.")

            print(f"\nInvalid values found in {col}:")

            for value in scheme_performance[col]:

                if not isinstance(value, (int, float)):
                    print(value)

    invalid_count = 0
    for index, row in scheme_performance.iterrows():

        exp = row["expense_ratio_pct"]

        if exp < 0.1 or exp > 2.5:
            invalid_count += 1
            print(f"{row['scheme_name']} -> Invalid Expense Ratio: {exp}")
    if invalid_count == 0:
        print("All expense ratios are within the valid range (0.1% to 2.5%).")
    
    save_processed(scheme_performance, "scheme_performance_cleaned.csv")

def clean_fund_master():
    fund_master = pd.read_csv("data/raw/01_fund_master.csv")
    inspect_dataset(fund_master)
    fund_master = parse_date(fund_master,"launch_date")
    save_processed(fund_master, "fund_master_cleaned.csv")

def clean_aum_by_fund_house():
    aum_by_fund_house = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
    inspect_dataset(aum_by_fund_house)
    aum_by_fund_house = parse_date(aum_by_fund_house,"date")
    save_processed(aum_by_fund_house, "aum_by_fund_house_cleaned.csv")

def clean_monthly_sip_inflows():
    monthly_sip_inflows = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
    inspect_dataset(monthly_sip_inflows)
    monthly_sip_inflows = parse_date(monthly_sip_inflows,"month")
    save_processed(monthly_sip_inflows, "monthly_sip_inflows_cleaned.csv")

def clean_category_inflows():
    category_inflows = pd.read_csv("data/raw/05_category_inflows.csv")
    inspect_dataset(category_inflows)
    category_inflows = parse_date(category_inflows,"month")
    save_processed(category_inflows, "category_inflows_cleaned.csv")

def clean_industry_folio_count():
    industry_folio_count = pd.read_csv("data/raw/06_industry_folio_count.csv")
    inspect_dataset(industry_folio_count)
    industry_folio_count = parse_date(industry_folio_count,"month")
    save_processed(industry_folio_count, "industry_folio_count_cleaned.csv")

def clean_portfolio_holdings():
    portfolio_holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
    inspect_dataset(portfolio_holdings)
    portfolio_holdings = parse_date(portfolio_holdings,"portfolio_date")
    save_processed(portfolio_holdings, "portfolio_holdings_cleaned.csv")

def clean_benchmark_indices():
    benchmark_indices = pd.read_csv("data/raw/10_benchmark_indices.csv")
    inspect_dataset(benchmark_indices)
    benchmark_indices = parse_date(benchmark_indices,"date")
    save_processed(benchmark_indices, "benchmark_indices_cleaned.csv")

if __name__ == "__main__":
    # clean_nav_history()
    # clean_investor_transactions()
    # clean_scheme_performance()
    # clean_fund_master()
    # clean_aum_by_fund_house()
    # clean_monthly_sip_inflows()
    # clean_category_inflows()
    # clean_industry_folio_count()
    # clean_portfolio_holdings()
    clean_benchmark_indices()