SELECT scheme_name,aum_crore 
FROM fact_performance fp 
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;

SELECT dd.year, dd.month, ROUND(AVG(fn.nav),2) AS avg_nav
FROM fact_nav fn
JOIN dim_date dd
ON fn.date_id = dd.date_id
GROUP BY dd.year, dd.month
ORDER BY dd.year, dd.month;

SELECT
    strftime('%Y', month) AS year,
    SUM(sip_inflow_crore) AS yearly_sip_inflow
FROM monthly_sip_inflows
GROUP BY year
ORDER BY year;

SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT scheme_name, expense_ratio_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

SELECT
    category,
    ROUND(AVG(return_3yr_pct),2) AS avg_return
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
GROUP BY category
ORDER BY avg_return DESC;

SELECT
    scheme_name,
    morningstar_rating
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
WHERE morningstar_rating = 5;

SELECT
    risk_category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category;

SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

SELECT
    category,
    ROUND(AVG(expense_ratio_pct),2) AS avg_expense_ratio
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
GROUP BY category
ORDER BY avg_expense_ratio;