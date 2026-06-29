# Mutual Fund Analysis Platform

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
├── sql/
├── dashboard/
├── reports/
│   └── charts/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── etl_pipeline.py
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* SQLAlchemy
* Requests
* Jupyter Notebook
* Git
* GitHub

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

## Current Status

* ✅ Project setup completed
* ✅ Dataset exploration completed
* ✅ AMFI code validation completed
* ✅ Live NAV extraction implemented
* ✅ ETL pipeline implemented
* ✅ Data cleaning completed
* ✅ SQLite data warehouse completed
* ✅ SQL analytical queries completed
* ✅ Data dictionary completed
* ✅ Exploratory Data Analysis completed
* 🔄 Dashboard development in progress

## Author

**Nuha Khan**
Data Analyst Intern @ Bluestock Fintech
