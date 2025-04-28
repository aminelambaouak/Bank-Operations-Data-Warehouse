# 🏦 Bank Operations Data Warehouse

![alt text](<Project diagram-1.png>)

Bank Operations Data Warehouse ETL
Project Overview
This project is focused on building a basic ETL (Extract, Transform, Load) pipeline for a Bank Operations Data Warehouse.
It demonstrates how to extract raw banking operations data from a CSV file, perform data cleaning and transformations, and then load the processed data into a MySQL database.

The pipeline is designed with a modular, object-oriented approach using Python and popular libraries such as Pandas and mysql-connector-python.

Main Features
Extraction:
Reads banking customer and transaction data from CSV files with handling of common file inconsistencies (e.g., malformed rows, encoding issues).

Transformation:
Cleans and standardizes the data, including:

Parsing and formatting operation times and dates.

Standardizing text fields.

Ensuring proper data types for all fields (dates, strings, etc.).

Loading:
Loads the cleaned data into a MySQL database for further use in analytics, reporting, and data warehousing activities.

Project Structure
etl.py:
Contains the ETL class with methods for extraction, transformation, and loading.

README.md:
Project description and instructions.

requirements.txt:
List of Python libraries needed for the project (e.g., pandas, mysql-connector-python).

Technologies Used
Python 3.x

Pandas for data manipulation

MySQL as the relational database

MySQL Connector for direct database connection

Power BI for data analysis and visualization

Potential Use Cases
Centralizing and cleaning customer banking data for operational reporting.

Building dashboards for transaction and customer activity monitoring.

Setting up the foundation for more complex ETL workflows and real-time data pipelines.

Supporting fraud detection, customer segmentation, or financial performance analysis.


![alt text](<Project workspace -1.png>)

--- 

📊 **Note**: This design prioritizes simplicity and maintainability, leveraging Python’s Pandas and mysql-connector for end-to-end pipeline control.  
