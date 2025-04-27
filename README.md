# 🏦 Bank Operations Data Warehouse

![image](https://github.com/user-attachments/assets/3914b700-a35f-42da-8fb8-c359224195c8)

## Overview  
This data warehouse consolidates and transforms raw data from **CRM** and **ERP systems** (via CSV files) into structured, analytics-ready datasets. Built using **Python (Pandas)** for data processing and **SQLAlchemy** with **MySQL** for storage, it follows a layered architecture (Bronze, Silver, Gold) to ensure reliability and scalability.

---

## Tools & Technologies  
- **Python**: Core ETL workflows powered by **Pandas** for data cleaning, transformations, and batch processing.  
- **SQLAlchemy**: Manages database interactions (e.g., MySQL table creation, queries, and transactions).  
- **MySQL**: Stores raw, cleaned, and aggregated data across all layers.  

---

## Data Sources  
- **CRM Data**: Customer profiles, interactions, and sales pipelines (CSV files).  
- **ERP Data**: Financial transactions, inventory logs, and operational metrics (CSV files).  

---

## Architecture Layers  
### 1. **Bronze Layer (Raw Data)**  
- **Purpose**: Ingestion of raw CSV files into Python with **Pandas**.  
- **Tools**:  
  - **Pandas**: Reads CSV files and performs initial schema validation.   
- **Object Type**: Raw tables stored "as-is" (e.g., `raw_crm_customers`, `raw_erp_transactions`).  

### 2. **Silver Layer (Cleaned & Standardized Data)**  
- **Purpose**: Clean, validate, and unify data for consistency.  
- **Tools**:  
  - **Pandas**: Handles deduplication, missing value imputation, and standardization (e.g., date formats, currency conversion).  
  - **SQLAlchemy**: Writes cleaned data to MySQL tables with enforced schemas and constraints.  
- **Processes**:  
  - Data enrichment (e.g., deriving `CustomerSegment` from transaction history).  
  - Normalization (e.g., splitting `Address` into `Street`, `City`, `ZipCode`).  

### 3. **Gold Layer (Business-Ready Data)**  
- **Purpose**: Deliver aggregated datasets optimized for analytics and reporting.  
- **Tools**:  
  - **Pandas**: Computes aggregations (e.g., monthly account balances, sales trends).  
  - **SQLAlchemy**: Creates MySQL views and tables for business-facing outputs.  
- **Outputs**:  
  - Star schema tables (e.g., `fact_sales`, `dim_customers`).  
  - Flat tables for dashboards (e.g., `customer_360_view`).  
  - Precomputed metrics (e.g., `TotalLoanPortfolio`, `AverageDepositByRegion`).  

---

## Key Workflows  
1. **Data Ingestion**:  
   - Pandas reads CRM/ERP CSV files, and SQLAlchemy loads them into MySQL Bronze tables.  
2. **Bronze → Silver**:  
   - Pandas cleans raw data (e.g., filtering invalid records) and writes to Silver tables via SQLAlchemy.  
3. **Silver → Gold**:  
   - Pandas calculates business metrics (e.g., customer lifetime value) and populates Gold-layer MySQL tables.  
4. **Batch Updates**:  
   - Scheduled Python scripts refresh data daily/weekly using Pandas and SQLAlchemy.  

---

## Outputs  
- **Gold Layer**:  
  - MySQL views for BI tools (e.g., Tableau, Power BI).  
  - Aggregated tables for regulatory compliance (e.g., liquidity reports).  
  - Enriched datasets for predictive modeling (e.g., churn prediction).  

---

## Benefits  
- **Cost Efficiency**: Open-source stack (Python + MySQL) avoids vendor lock-in.  
- **Auditability**: Full traceability from raw CSV files to final metrics.  
- **Flexibility**: Pandas enables rapid iteration on transformation logic.  

![alt text](<Project workspace -1.png>)

--- 

📊 **Note**: This design prioritizes simplicity and maintainability, leveraging Python’s Pandas and SQLAlchemy for end-to-end pipeline control.  
