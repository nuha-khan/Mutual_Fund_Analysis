# Mutual Fund Analysis – Data Dictionary

## Overview

This document describes the database schema used in the Mutual Fund Analysis project. It includes the table names, column names, data types, business definitions, and data sources.

---

# Table: dim_fund

**Description:** Stores master information about mutual fund schemes.

**Source:** `fund_master_cleaned.csv`

| Column      | Data Type | Business Definition                                |
| ----------- | --------- | -------------------------------------------------- |
| amfi_code   | INTEGER   | Unique AMFI code identifying a mutual fund scheme. |
| scheme_name | TEXT      | Name of the mutual fund scheme.                    |
| fund_house  | TEXT      | Asset Management Company (AMC).                    |
| category    | TEXT      | Scheme category (Large Cap, Mid Cap, etc.).        |
| plan        | TEXT      | Direct or Regular plan.                            |
| launch_date | DATE      | Scheme launch date.                                |

---

# Table: dim_date

**Description:** Date dimension used by all fact tables.

**Source:** Derived from all datasets containing date fields.

| Column  | Data Type | Business Definition        |
| ------- | --------- | -------------------------- |
| date_id | INTEGER   | Surrogate primary key.     |
| date    | DATE      | Calendar date.             |
| day     | INTEGER   | Day of month.              |
| month   | INTEGER   | Month number (1–12).       |
| year    | INTEGER   | Calendar year.             |
| quarter | INTEGER   | Quarter of the year (1–4). |

---

# Table: fact_nav

**Description:** Stores historical daily Net Asset Value (NAV).

**Source:** `nav_history_cleaned.csv`

| Column    | Data Type | Business Definition                  |
| --------- | --------- | ------------------------------------ |
| nav_id    | INTEGER   | Surrogate primary key.               |
| amfi_code | INTEGER   | Foreign key to dim_fund.             |
| date_id   | INTEGER   | Foreign key to dim_date.             |
| nav       | REAL      | Daily Net Asset Value of the scheme. |

---

# Table: fact_aum

**Description:** Stores Assets Under Management (AUM) information.

**Source:** `aum_by_fund_house_cleaned.csv`

| Column      | Data Type | Business Definition                          |
| ----------- | --------- | -------------------------------------------- |
| aum_id      | INTEGER   | Surrogate primary key.                       |
| fund_house  | TEXT      | Asset Management Company.                    |
| date_id     | INTEGER   | Foreign key to dim_date.                     |
| aum_lakh    | REAL      | Assets Under Management (₹ lakh crore).      |
| aum_crore   | REAL      | Assets Under Management (₹ crore).           |
| num_schemes | INTEGER   | Number of schemes managed by the fund house. |

---

# Table: fact_performance

**Description:** Stores scheme performance metrics.

**Source:** `scheme_performance_cleaned.csv`

| Column             | Data Type | Business Definition                        |
| ------------------ | --------- | ------------------------------------------ |
| performance_id     | INTEGER   | Surrogate primary key.                     |
| amfi_code          | INTEGER   | Foreign key to dim_fund.                   |
| return_1y          | REAL      | One-year return (%).                       |
| return_3y          | REAL      | Three-year return (%).                     |
| return_5y          | REAL      | Five-year return (%).                      |
| benchmark_return   | REAL      | Benchmark return (%).                      |
| alpha              | REAL      | Risk-adjusted excess return.               |
| beta               | REAL      | Market volatility measure.                 |
| sharpe_ratio       | REAL      | Risk-adjusted performance metric.          |
| sortino_ratio      | REAL      | Downside-risk-adjusted performance metric. |
| std_dev            | REAL      | Standard deviation of returns.             |
| max_drawdown       | REAL      | Maximum observed loss from peak.           |
| aum_crore          | REAL      | Assets Under Management (₹ crore).         |
| expense_ratio      | REAL      | Annual expense ratio (%).                  |
| morningstar_rating | INTEGER   | Morningstar rating (1–5).                  |
| risk_grade         | TEXT      | Risk classification of the scheme.         |

---

# Table: fact_transactions

**Description:** Stores investor transaction details.

**Source:** `transactions_cleaned.csv`

| Column           | Data Type | Business Definition               |
| ---------------- | --------- | --------------------------------- |
| transaction_id   | INTEGER   | Unique transaction identifier.    |
| investor_id      | TEXT      | Investor identifier.              |
| amfi_code        | INTEGER   | Foreign key to dim_fund.          |
| date_id          | INTEGER   | Foreign key to dim_date.          |
| transaction_type | TEXT      | SIP, Redemption, or Lumpsum.      |
| amount           | REAL      | Transaction amount (₹).           |
| state            | TEXT      | Investor's state.                 |
| city             | TEXT      | Investor's city.                  |
| city_tier        | TEXT      | T30 or B30 classification.        |
| age_group        | TEXT      | Investor age category.            |
| gender           | TEXT      | Investor gender.                  |
| annual_income    | REAL      | Annual income (₹ lakh).           |
| payment_mode     | TEXT      | Mode of payment.                  |
| kyc_status       | TEXT      | Investor KYC verification status. |

---

# Additional Analytical Tables

The following datasets are stored for SQL analysis and EDA:

* monthly_sip_inflows
* category_inflows
* industry_folio_count
* portfolio_holdings
* benchmark_indices

These tables retain their original cleaned CSV structure and serve as supporting analytical datasets.
