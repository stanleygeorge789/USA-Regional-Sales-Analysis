# USA Regional Sales Analysis

Exploratory Data Analysis of Acme Co.’s USA sales data from 2014 to 2018, focused on revenue trends, profitability drivers, regional performance, and customer segmentation. This project demonstrates end-to-end EDA using Python and produces analysis-ready outputs suitable for BI and dashboarding.

## Project Objective

The objective of this project is to analyze historical sales data and answer the following business questions:

- How does revenue trend over time and across months?
- Which products, channels, and regions drive the most revenue and profit?
- Are profit margins influenced more by pricing or by volume?
- Where do pricing, revenue, and order-value outliers exist?
- How are customers distributed by revenue and profitability?

## Dataset Overview

The analysis uses a multi-sheet Excel dataset with the following components:

- Sales Orders: 64,104 rows
- Customers: 175 rows
- Products: 30 rows
- Regions and State mappings
- Product-level budgets for 2017

Final cleaned dataset:

- Rows: 64,104
- Columns: 15
- Time range: 2014–2018  
- Note: 2018 data is partial and excluded from seasonality analysis

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Data Preparation

Key data preparation steps:

- Loaded all Excel sheets and validated schema
- Corrected malformed headers in the State Regions sheet
- Checked and confirmed no duplicate sales records
- Merged sales data with customer, product, and regional datasets
- Standardized column names using snake_case
- Removed unused and redundant fields
- Converted data types and validated date fields
- Nullified budget values for non-2017 orders
- Exported cleaned and processed datasets for reuse

## Feature Engineering

The following derived features were created:

- `total_cost` = quantity × cost
- `profit` = revenue − total_cost
- `profit_margin_pct`
- `order_month_name`
- `order_month_num`
- Monthly aggregation keys for time series analysis

## Exploratory Analysis

The notebook includes the following analyses:

- Monthly revenue trend over time
- Aggregated seasonality by calendar month
- Top 10 products by total revenue
- Top 10 products by average profit margin
- Sales distribution by channel
- Average order value distribution
- Profit margin versus unit price relationship
- Unit price variability by product
- Total sales by US region
- State-level sales performance using a choropleth map
- Top and bottom customers by revenue
- Customer segmentation using revenue vs profit margin
- Correlation analysis of numeric variables

## Key Insights

- Monthly revenue remains stable between approximately $23M and $26.5M from 2014 to 2017
- A sharp revenue decline occurs in early 2017, indicating a possible one-time disruption
- Wholesale accounts for 54% of total sales, while exports contribute only 15%
- Product revenue is highly concentrated, with Products 26 and 25 significantly outperforming others
- Profit margins range from approximately 18% to 60%, with no strong correlation to unit price
- Unit price is a stronger driver of revenue and profit than order quantity
- The West region leads sales, with California contributing roughly $230M alone
- Customer revenue is heavily concentrated among the top-performing accounts

## Business Recommendations

- Exclude or explicitly classify bulk and promotional outliers when computing averages
- Apply pricing and margin strategies from top-performing products to mid-tier products
- Expand export channels to reduce dependence on domestic wholesale sales
- Investigate the early 2017 revenue anomaly before seasonal planning
- Use aggregated outputs as direct inputs for Power BI dashboards

## Output Files

- `USA Regional Analysis.ipynb`
- `Sales_data(EDA Exported).csv`
- `final.csv`

## Next Steps

- Build executive dashboards in Power BI
- Add revenue forecasting and trend projection
- Perform customer cohort and retention analysis
- Extend analysis using post-2018 data
