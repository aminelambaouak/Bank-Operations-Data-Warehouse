import pandas as pd
import mysql.connector



# extraction of data from the CSV file
def extract_data(file_path):
    df = pd.read_csv(file_path, encoding="utf-8")
    return df


# transforming and cleaning data 
def parse_time(time_string):
    try:
        # Try parsing as 12-hour format with AM/PM
        return pd.to_datetime(time_string, format='%I:%M %p').time()
    except ValueError:
        # If it fails, try parsing as 24-hour format
        return pd.to_datetime(time_string, format='%H:%M:%S').time()

# Apply the function to the 'operation_time' column (inside the transform_data function)
def transform_data(df):
    # Apply time parsing on 'operation_time' if it exists in the dataframe
    if 'operation_time' in df.columns:
        df['operation_time'] = df['operation_time'].apply(parse_time)
    
    # Convert 'operation_date' to datetime if it exists
    if 'operation_date' in df.columns:
        df['operation_date'] = pd.to_datetime(df['operation_date'])

    # Convert 'account_open_date' and 'birth_date' to datetime if they exist in df1
    list_date = ['account_open_date', 'birth_date']
    for item in list_date:
        if item in df.columns:
            df[item] = pd.to_datetime(df[item])
    
    # Convert specified columns to string
    list_string = ['first_name', 'last_name', 'gender', 'email', 'phone_number', 'address', 'city', 
                   'country', 'account_type', 'account_number', 'operation_id', 'transaction_type', 'currency', 'channel']
    for item in list_string:
        if item in df.columns:
            df[item] = df[item].astype('string')
            
    df['client_id'].drop_duplicates(inplace=True)

    return df

# define csv files path
df_customers = extract_data('C:\\Users\\amine\\Downloads\\Accounts.csv')
df_customers_transformed = transform_data(df_customers)
df_operations = extract_data('C:\\Users\\amine\\Downloads\\The_operations (5).csv')
df_operations_transformed = transform_data(df_operations)

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="*****",
    database = 'Bankdwproject'

)

# Create a cursor object to interact with the database
myCursor = mydb.cursor()

# Create the new database if it does not exist
myCursor.execute("CREATE DATABASE IF NOT EXISTS BankDWProject")

# Confirm that the database was created by listing the databases
myCursor.execute("SHOW DATABASES")

# Fetch and print the databases
for db in myCursor:
    print(db)
    
# load data in Mysql
myCursor.execute("""CREATE TABLE IF NOT EXISTS BankOperations(
                                                            operation_id VARCHAR(50),
                                                            client_id INT PRIMARY KEY,
                                                            transaction_type VARCHAR(50), 
                                                            amount FLOAT, 
                                                            currency VARCHAR(10),
                                                            operation_date DATE,
                                                            operation_time VARCHAR(10), 
                                                            balance_after_transaction INT,
                                                            channel VARCHAR(50));""")

    
myCursor.execute("""CREATE TABLE IF NOT EXISTS BankCustomers(
                                                            client_id INT PRIMARY KEY, 
                                                            first_name VARCHAR(50), 
                                                            last_name VARCHAR(50), 
                                                            birth_date DATE, 
                                                            gender VARCHAR(50), 
                                                            email VARCHAR(50),
                                                            phone_number VARCHAR(50), 
                                                            address VARCHAR(100), 
                                                            city VARCHAR(50), 
                                                            country VARCHAR(50), 
                                                            account_open_date DATE,
                                                            account_type VARCHAR(50), 
                                                            account_number VARCHAR(50), 
                                                            account_status VARCHAR(50));""")
    
myCursor.execute("SHOW TABLES")
for table in myCursor:
    print(table)


myCursor.execute("DELETE FROM BankCustomers")
myCursor.execute("DELETE FROM BankOperations")
mydb.commit()

#inserting customers data
insert_customers_query = """INSERT INTO BankCustomers VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

#inserting opearations data
insert_operations_query = """INSERT INTO BankOperations VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

#iterationg over rows of each table to load data in mysql
for i, row in df_customers_transformed.iterrows():
    myCursor.execute(insert_customers_query, tuple(row))
    
for i, row in df_operations_transformed.iterrows():
    myCursor.execute(insert_operations_query, tuple(row))

# Commit the changes
mydb.commit()

# Close the connection
mydb.close()
