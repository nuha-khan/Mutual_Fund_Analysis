# Mutual Fund Analysis Platform

A data analytics project focused on analyzing Indian mutual fund data through ETL pipelines, data validation, exploratory analysis, SQL-based analytics, and reporting.

## Project Objectives

- Extract and validate mutual fund data from provided datasets and public APIs.
- Build a reusable ETL pipeline for data ingestion, validation, and preprocessing.
- Perform exploratory data analysis on mutual fund datasets.
- Prepare cleaned datasets for SQL database integration and dashboarding.
- Generate insights on fund performance and investment trends.

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
│
├── data_ingestion.py
├── live_nav_fetch.py
├── etl_pipeline.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- Requests
- Git
- GitHub

## Work Completed

### Day 1 – Data Ingestion & Validation

- Downloaded and organized project datasets.
- Explored dataset structure and metadata.
- Extracted unique fund houses, categories, sub-categories, and risk categories.
- Implemented live NAV extraction using the mfapi.in API.
- Validated AMFI codes between `fund_master` and `nav_history`.
- Performed initial data quality assessment and documented observations.

### Day 2 – ETL Pipeline & Data Cleaning

- Developed a reusable ETL pipeline for dataset preprocessing.
- Implemented reusable helper functions for:
  - Dataset inspection
  - Date parsing and validation
  - Processed file generation
- Cleaned and validated all project datasets.
- Standardized date formats across datasets.
- Validated NAV values, transaction amounts, numeric return fields, and expense ratios.
- Performed missing value, duplicate record, and categorical value inspection.
- Generated cleaned datasets in the `data/processed` directory for downstream analysis.

## Current Status

- ✅ Project setup completed
- ✅ Dataset exploration completed
- ✅ AMFI code validation completed
- ✅ Live NAV extraction implemented
- ✅ ETL pipeline implemented
- ✅ Data cleaning completed
- 🔄 SQLite database design in progress
- 🔄 SQL analytical queries in progress

## Author

**Nuha Khan**  
Data Analyst Intern @ Bluestock Fintech
