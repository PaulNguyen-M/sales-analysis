# Module 2: Data Analysis

## Dataset

* 850 transaction records
* Includes product, customer, revenue, and promotion data

## Data Pipeline

1. Data Understanding
2. Data Cleaning
3. Feature Engineering
4. Exploratory Data Analysis (EDA)

## Data Cleaning

* Converted date column to datetime
* Removed missing values
* Checked negative revenue and anomalies

## Feature Engineering

* Profit = Revenue - Cost
* Month extracted from transaction date
* Promotion flag (Has_Promo)

## Analysis Performed

* Revenue by product
* Profit by product
* Customer contribution analysis
* Promotion effectiveness
* Revenue trends over time

## Key Insights

* A small number of products contribute the majority of revenue (Pareto Principle)
* Some transactions result in negative profit
* Promotions do not always increase revenue
* A few customers contribute significantly to total revenue

## Structure

* data/: raw → cleaned → final
* notebooks/: step-by-step analysis
* sql/: analytical queries
* reports/: insights and final report

## Tools Used

* Python (Pandas)
* SQL
* Excel (Pivot Table)
