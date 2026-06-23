# Data Quality Summary – Day 1

## Dataset Review

The provided datasets were successfully downloaded and loaded using Pandas for initial inspection.

## Initial Observations

* Dataset structures were reviewed using shape, data types, and sample records.
* Fund metadata and NAV history datasets were identified and mapped to the project requirements.
* API metadata for scheme code 125497 returned "SBI Small Cap Fund - Direct Plan - Growth", whereas the project description references "HDFC Top 100 Direct". This discrepancy has been noted for verification.
* No detailed cleaning or transformation has been performed at this stage.

## Data Quality Observation #1: Scheme Code Validation Across Sources

A validation check was performed between the project task description, the provided `fund_master.csv` dataset, and the external `mfapi.in` API.

Findings:

* The scheme codes and scheme names listed in the task description matched the records present in `fund_master.csv`.
* However, multiple scheme codes returned different scheme names when queried through the `mfapi.in` API.

Example:

AMFI Code: 119551

* Task Description: SBI Bluechip Fund
* fund_master.csv: SBI Bluechip Fund
* mfapi.in API: Aditya Birla Sun Life Banking & PSU Debt Fund - Direct - IDCW

Similar discrepancies were observed for several of the specified scheme codes.

Conclusion:

The task description and provided project datasets appear internally consistent. However, inconsistencies exist between the project data and the external API responses. For project analysis and validation, the provided datasets will be treated as the primary source of truth, while API data will be used specifically for demonstrating live NAV extraction.

