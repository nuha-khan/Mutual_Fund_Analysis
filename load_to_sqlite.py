import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///sql/bluestock_mf.db")

# with open("sql/schema.sql","r") as file:
#     schema = file.read()

# with engine.begin() as connection:
#     statements = schema.split(";")

#     for statement in statements:
#         statement = statement.strip()

#         if statement:
#             connection.exec_driver_sql(statement)


def verify_row_count(df, table_name):
    csv_rows = len(df)
    db_rows = pd.read_sql(f"SELECT COUNT(*) AS total FROM {table_name}", con=engine)

    print("CSV rows =", csv_rows)
    print("DB rows =", db_rows["total"][0])

    if csv_rows == db_rows["total"][0]:
        print("Row count verification successful!")
    else:
        print("Row count mismatch!")

def load_csv(file_path, date_column=None):
    df = pd.read_csv(file_path)

    if date_column:
        df[date_column] = pd.to_datetime(df[date_column])

    return df

def load_fact_table(
    df,
    table_name,
    id_column,
    date_column,
    final_columns
):
    # Read date lookup
    dim_date_lookup = pd.read_sql(
        "SELECT date_id, date FROM dim_date",
        con=engine
    )

    dim_date_lookup["date"] = pd.to_datetime(dim_date_lookup["date"])

    # Merge to get date_id
    df = df.merge(
        dim_date_lookup,
        left_on=date_column,
        right_on="date",
        how="left"
    )

    # Remove original date columns
    df = df.drop(columns=[date_column, "date"])

    # Generate primary key
    df.insert(
        0,
        id_column,
        range(1, len(df) + 1)
    )

    # Arrange columns
    df = df[final_columns]

    # Load into SQLite
    df.to_sql(
        table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    # Verify
    verify_row_count(df, table_name)

    return df

# fund_master = pd.read_csv("data/processed/fund_master_cleaned.csv")
# fund_master = fund_master.drop(columns=["expense_ratio_pct", "exit_load_pct"])
# fund_master.to_sql("dim_fund",con=engine,if_exists="append",index=False)
# verify_row_count(fund_master, "dim_fund")

# nav_history = load_csv("data/processed/nav_history_cleaned.csv", "date")
# transactions = load_csv("data/processed/transactions_cleaned.csv", "transaction_date")
# fund_master = load_csv("data/processed/fund_master_cleaned.csv", "launch_date")
# aum = load_csv("data/processed/aum_by_fund_house_cleaned.csv", "date")
# monthly_sip = load_csv("data/processed/monthly_sip_inflows_cleaned.csv", "month")
# category = load_csv("data/processed/category_inflows_cleaned.csv", "month")
# industry = load_csv("data/processed/industry_folio_count_cleaned.csv", "month")
# portfolio = load_csv("data/processed/portfolio_holdings_cleaned.csv", "portfolio_date")
benchmark = load_csv("data/processed/benchmark_indices_cleaned.csv", "date")
# performance = load_csv("data/processed/scheme_performance_cleaned.csv")

# def create_dim_date(*date_columns):
#     all_dates = pd.concat(date_columns)
#     all_dates = all_dates.drop_duplicates()
#     all_dates = all_dates.sort_values().reset_index(drop=True)

#     dim_date = pd.DataFrame()
#     dim_date["date_id"] = range(1, len(all_dates) + 1)
#     dim_date["date"] = all_dates
#     dim_date["day"] = dim_date["date"].dt.day
#     dim_date["month"] = dim_date["date"].dt.month
#     dim_date["year"] = dim_date["date"].dt.year
#     dim_date["quarter"] = dim_date["date"].dt.quarter

#     return dim_date

# dim_date = create_dim_date(nav_history["date"],transactions["transaction_date"],fund_master["launch_date"],aum["date"],
#     monthly_sip["month"],category["month"],industry["month"],portfolio["portfolio_date"],benchmark["date"])

# dim_date.to_sql("dim_date",con=engine,if_exists="append",index=False)
# verify_row_count(dim_date, "dim_date")

# fact_nav = load_fact_table(df=nav_history.copy(),table_name="fact_nav",id_column="nav_id",date_column="date",
#     final_columns=["nav_id","amfi_code","date_id","nav"])

# fact_aum = load_fact_table(df=aum.copy(),table_name="fact_aum",id_column="aum_id",date_column="date",
#     final_columns=["aum_id","date_id","fund_house","aum_lakh_crore","aum_crore","num_schemes"])

# fact_transactions = load_fact_table(df=transactions.copy(),table_name="fact_transactions",id_column="transaction_id",date_column="transaction_date",
#     final_columns=["transaction_id","investor_id","date_id","amfi_code","transaction_type","amount_inr","state",
#         "city","city_tier","age_group","gender","annual_income_lakh","payment_mode","kyc_status"])

# fact_performance = performance.copy()
# fact_performance.insert(0,"performance_id",range(1, len(fact_performance) + 1))
# fact_performance = fact_performance[["performance_id","amfi_code","return_1yr_pct","return_3yr_pct","return_5yr_pct",
#                                      "benchmark_3yr_pct","alpha","beta","sharpe_ratio","sortino_ratio","std_dev_ann_pct",
#                                      "max_drawdown_pct","aum_crore","expense_ratio_pct","morningstar_rating","risk_grade"]]

# fact_performance.to_sql("fact_performance",con=engine,if_exists="append",index=False)
# verify_row_count(fact_performance,"fact_performance")

# monthly_sip.to_sql("monthly_sip_inflows",con=engine,if_exists="replace",index=False)
# verify_row_count(monthly_sip,"monthly_sip_inflows")

# category.to_sql("category_inflows",con=engine,if_exists="replace",index=False)
# verify_row_count(category,"category_inflows")

# industry.to_sql("industry_folio_count",con=engine,if_exists="replace",index=False)
# verify_row_count(industry,"industry_folio_count")

# portfolio.to_sql("portfolio_holdings",con=engine,if_exists="replace",index=False)
# verify_row_count(portfolio,"portfolio_holdings")

benchmark.to_sql("benchmark_indices",con=engine,if_exists="replace",index=False)
verify_row_count(benchmark,"benchmark_indices")