import pandas as pd

# extraction of data from the CSV file
def extract_data(file_path):
    df = pd.read_csv(file_path, encoding="utf-8")
    return df.head()

df1 = extract_data("C:\\Users\\amine\\Downloads\\Accounts.csv")
df2 = extract_data("C:\\Users\\amine\\Downloads\\The_operations (5).csv")

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

    return df.head()
print(df1.head())

# connect my script to Mysql database
