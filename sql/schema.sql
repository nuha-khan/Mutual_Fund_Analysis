CREATE TABLE IF NOT EXISTS dim_fund(
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT NOT NULL,
    scheme_name TEXT NOT NULL,
    category TEXT NOT NULL,
    sub_category TEXT NOT NULL,
    plan TEXT NOT NULL,
    launch_date DATE NOT NULL,
    benchmark TEXT NOT NULL,
    min_sip_amount INTEGER NOT NULL,
    min_lumpsum_amount INTEGER NOT NULL,
    fund_manager TEXT NOT NULL,
    risk_category TEXT NOT NULL,
    sebi_category_code TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    day INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    nav REAL NOT NULL,

    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS fact_aum (
    aum_id INTEGER PRIMARY KEY,
    date_id INTEGER NOT NULL,
    fund_house TEXT NOT NULL,
    aum_lakh_crore REAL NOT NULL,
    aum_crore INTEGER NOT NULL,
    num_schemes INTEGER NOT NULL,

    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER NOT NULL,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,

    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,

    aum_crore INTEGER,
    expense_ratio_pct REAL,
    morningstar_rating INTEGER,
    risk_grade TEXT,

    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id TEXT NOT NULL,
    date_id INTEGER NOT NULL,
    amfi_code INTEGER NOT NULL,

    transaction_type TEXT NOT NULL,
    amount_inr INTEGER NOT NULL,

    state TEXT,
    city TEXT,
    city_tier TEXT,

    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,

    payment_mode TEXT,
    kyc_status TEXT,

    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);
