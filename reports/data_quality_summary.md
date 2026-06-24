# Data Quality Summary – Day 1

## Dataset Review

The provided mutual fund datasets were successfully downloaded, organized, and loaded using Pandas for initial exploration and validation. Initial inspection was performed to understand dataset structure, contents, and relationships between files.

## Initial Observations

* Dataset structures were reviewed using shape, data types, column names, and sample records.
* Fund metadata (`fund_master.csv`) and NAV history (`nav_history.csv`) were identified and mapped to the project requirements.
* Unique fund houses, categories, sub-categories, and risk categories were extracted and reviewed.
* Live NAV data was successfully fetched from the `mfapi.in` API for testing and validation purposes.
* No detailed data cleaning, transformation, or imputation has been performed at this stage.

## Data Validation

### AMFI Code Validation

A validation check was performed between `fund_master.csv` and `nav_history.csv` to verify dataset consistency.

**Result:**

* All AMFI codes present in `fund_master.csv` were successfully found in `nav_history.csv`.
* No missing AMFI codes were identified.
* The two datasets appear internally consistent and suitable for further analysis.

## Data Quality Observation #1: Scheme Code Validation Across Sources

A validation check was performed between the project task description, the provided `fund_master.csv` dataset, and the external `mfapi.in` API.

### Findings

* The scheme codes and scheme names listed in the task description matched the records present in `fund_master.csv`.
* However, multiple scheme codes returned different scheme names when queried through the `mfapi.in` API.

**Example**

AMFI Code: **119551**

* Task Description: SBI Bluechip Fund
* `fund_master.csv`: SBI Bluechip Fund
* `mfapi.in` API: Aditya Birla Sun Life Banking & PSU Debt Fund - Direct - IDCW

Similar discrepancies were observed for several of the specified scheme codes.

### Conclusion

The task description and provided project datasets appear internally consistent. However, inconsistencies exist between the project data and the external API responses. For project analysis and validation, the provided datasets will be treated as the primary source of truth, while API data will be used specifically for demonstrating live NAV extraction functionality.

## Next Steps

* Perform detailed data profiling on all datasets.
* Identify missing values, duplicate records, and data type inconsistencies.
* Begin exploratory data analysis (EDA).
* Prepare datasets for transformation and loading into the target database.
