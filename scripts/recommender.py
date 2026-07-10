import pandas as pd

# Load datasets
fund_master = pd.read_csv("../data/processed/fund_master_cleaned.csv")
scorecard = pd.read_csv("../data/processed/fund_scorecard.csv")

# Merge datasets
funds = scorecard.merge(fund_master[['amfi_code', 'risk_category']], on='amfi_code', how='left')

# User Input
risk = input("Enter Risk Appetite (Low / Moderate / High): ").strip().lower()

# Map user input to dataset categories
risk_map = {
    "low": ["Low"],
    "moderate": ["Moderate"],
    "high": ["High", "Moderately High", "Very High"]
}

# Validate input
if risk not in risk_map:
    print("Please enter Low, Moderate or High.")
else:

    recommended = funds[
        funds["risk_category"].isin(risk_map[risk])
    ]

    recommended = (recommended.sort_values(by="Sharpe_Ratio", ascending=False).head(3))

    print("\nTop 3 Recommended Funds\n")

    print(recommended[
            [
                "scheme_name",
                "risk_category",
                "Sharpe_Ratio",
                "Fund_Score"
            ]
        ]
    )