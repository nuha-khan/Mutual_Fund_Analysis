# Mutual Fund Analytics Platform

A data analytics project focused on analyzing Indian mutual fund data through ETL pipelines, data validation, exploratory analysis, SQL-based analytics, and reporting.

## Project Objectives

* Extract and validate mutual fund data from provided datasets and public APIs.
* Build a reusable ETL pipeline for data ingestion, validation, and preprocessing.
* Perform exploratory data analysis on mutual fund datasets.
* Prepare cleaned datasets for SQL database integration and dashboarding.
* Generate insights on fund performance, investor behavior, and investment trends.

## Project Structure

```text
Mutual_Fund_Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── Advanced_Analytics.ipynb
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   ├── data_ingestion.py
│   └── etl_pipeline.py
│
├── sql/
├── dashboard/
├── reports/
│  
│
├── scripts/
│   ├── live_nav_fetch.py
│   └── load_to_sqlite.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SQLite
- SQLAlchemy
- Power BI
- Requests
- Jupyter Notebook
- Git
- GitHub

## Work Completed

### Day 1 – Data Ingestion & Validation

* Downloaded and organized project datasets.
* Explored dataset structure and metadata.
* Extracted unique fund houses, categories, sub-categories, and risk categories.
* Implemented live NAV extraction using the mfapi.in API.
* Validated AMFI codes between `fund_master` and `nav_history`.
* Performed initial data quality assessment and documented observations.

### Day 2 – ETL Pipeline, SQLite Data Warehouse & SQL Analytics

* Developed a reusable ETL pipeline for dataset preprocessing.
* Implemented reusable helper functions for dataset inspection, date parsing, validation, and processed file generation.
* Cleaned and validated all project datasets.
* Standardized date formats across datasets.
* Validated NAV values, transaction amounts, numeric return fields, and expense ratios.
* Performed missing value, duplicate record, and categorical value inspection.
* Generated cleaned datasets in the `data/processed` directory.
* Designed and implemented a SQLite star schema.
* Created dimension tables:

  * `dim_fund`
  * `dim_date`
* Created fact tables:

  * `fact_nav`
  * `fact_aum`
  * `fact_performance`
  * `fact_transactions`
* Loaded cleaned datasets into SQLite using SQLAlchemy.
* Added supporting analytical tables:

  * `monthly_sip_inflows`
  * `category_inflows`
  * `industry_folio_count`
  * `portfolio_holdings`
  * `benchmark_indices`
* Implemented row count verification after loading each table.
* Wrote and tested 10 analytical SQL queries.
* Created a comprehensive data dictionary documenting tables, columns, data types, business definitions, and data sources.

### Day 3 – Exploratory Data Analysis (EDA)

Performed a comprehensive exploratory data analysis using SQL, Pandas, Matplotlib, Seaborn, and Plotly.

#### Visualizations Created

1. NAV Trend Analysis (Top 5 Funds)
2. AUM Growth by Fund House
3. Monthly SIP Inflow Trend
4. Category-wise Monthly Inflows Heatmap
5. Investor Age Group Distribution
6. SIP Investment Distribution by Age Group (Box Plot)
7. Gender Distribution of Investors
8. Geographic Distribution of SIP Investments by State
9. T30 vs B30 City Tier Distribution
10. Industry Folio Count Growth Trend
11. NAV Correlation Heatmap (Top Performing Funds)
12. Sector Allocation Donut Chart
13. Payment Mode Distribution
14. KYC Status Distribution
15. Transaction Type Distribution
16. Annual Income Group Analysis

#### Key Insights

* Identified long-term NAV trends across leading mutual fund schemes.
* Compared AUM growth across major fund houses.
* Analyzed monthly SIP inflows and highlighted peak investment periods.
* Visualized category-wise fund inflows using heatmaps.
* Explored investor demographics through age, gender, and income analyses.
* Studied SIP investment behavior across different age groups.
* Examined geographic participation by state and city tier (T30 vs B30).
* Evaluated industry folio growth over time.
* Investigated NAV correlations among top-performing schemes.
* Aggregated equity sector allocations across portfolios.
* Analyzed payment modes, KYC status, and transaction types.

## Day 4 – Interactive Power BI Dashboard

Developed a multi-page interactive Power BI dashboard to visualize key mutual fund industry metrics, fund performance, investor analytics, and SIP trends.

### Dashboard Pages

#### Page 1 – Industry Overview

- KPI Cards for:
  - Total Assets Under Management (AUM)
  - Monthly SIP Inflows
  - Total Folios
  - Total Mutual Fund Schemes
- Industry AUM Trend (2022–2025)
- AUM by Fund House
- Interactive slicers for Year and Fund House

#### Page 2 – Fund Performance Analysis

- Risk vs Return Scatter Plot
- NAV vs Benchmark Trend Comparison
- Top 10 Funds by Fund Score
- Dynamic filtering by Category and Fund House

#### Page 3 – NAV Detail Analysis

- Drill-through page from Fund Performance
- NAV Trend over Time
- Fund Information Cards:
  - Scheme Name
  - Fund House
  - Category
  - Launch Date
- Interactive navigation and tooltips

#### Page 4 – SIP & Market Trends

- Monthly SIP Inflow Trend
- SIP Inflow vs Benchmark Index Comparison
- Interactive Year slicer
- Tooltips for all visuals

### Dashboard Features

- Built using Power BI Desktop
- Connected to SQLite data warehouse
- Interactive slicers
- Drill-through navigation
- Custom tooltips
- Consistent Bluestock-themed dashboard design
- Exported dashboard as `.pbix` and PDF

## Day 5 – Advanced Performance Analytics

Implemented advanced quantitative analytics commonly used in mutual fund performance evaluation.

### Analytics Implemented

1. Alpha & Beta Calculation (Linear Regression)
2. Maximum Drawdown Analysis
3. Fund Scorecard (0–100 Composite Ranking)
4. Benchmark Comparison (Top 5 Funds vs NIFTY50 & NIFTY100)
5. Tracking Error Calculation

### Methodologies Used

- Daily Return Computation
- Linear Regression using `scipy.stats.linregress`
- Annualized Alpha Estimation
- Beta Calculation against Benchmark
- Maximum Drawdown using Running Peak Method
- Tracking Error:
  - Standard Deviation of (Fund Return − Benchmark Return)
  - Annualized using √252
- Composite Fund Score based on:
  - 30% → 3-Year CAGR Rank
  - 25% → Sharpe Ratio Rank
  - 20% → Alpha Rank
  - 15% → Expense Ratio Rank (Inverse)
  - 10% → Maximum Drawdown Rank (Inverse)

### Outputs Generated

- `alpha_beta.csv`
- `fund_scorecard.csv`
- Benchmark Comparison Visualization

## Current Status

- ✅ Project setup completed
- ✅ Dataset exploration completed
- ✅ Live NAV extraction implemented
- ✅ ETL pipeline completed
- ✅ Data cleaning & preprocessing completed
- ✅ SQLite data warehouse implemented
- ✅ SQL analytical queries completed
- ✅ Data dictionary prepared
- ✅ Exploratory Data Analysis completed
- ✅ Interactive Power BI Dashboard completed
- ✅ Advanced Performance Analytics completed

## Author

**Nuha Khan**
Data Analyst Intern @ Bluestock Fintech
