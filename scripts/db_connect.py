import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="070193"
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

# Close the cursor and connection when done
myCursor.close()
mydb.close()