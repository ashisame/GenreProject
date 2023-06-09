import pandas as pd
import mysql.connector
from config import db_host, db_user, db_password, db_database

# Establishing a Connection to the MariaDB database
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

# Creating a cursor to execute SQL queries
cursor = connection.cursor()

# Altering table queries to rename columns
queries = [
    "ALTER TABLE `moviesdataset` RENAME COLUMN `YEAR` TO `RELEASE_YEAR`",
    "ALTER TABLE `moviesdataset` RENAME COLUMN `Gross` TO `GROSS`",
    "ALTER TABLE `moviesdataset` RENAME COLUMN `RunTime` TO `RUNTIME`"
]

# Executing ALTER TABLE queries
for query in queries:
    cursor.execute(query)

# Updating queries using the REGEXP_REPLACE() function and string manipulation functions
queries = [
    "UPDATE moviesdataset SET RELEASE_YEAR = REGEXP_REPLACE(RELEASE_YEAR, '\\(I\\)|\\(II\\)|\\(III\\)|\\(IV\\)', '') WHERE RELEASE_YEAR REGEXP '\\(I\\)|\\(II\\)|\\(III\\)|\\(IV\\)'",
    "UPDATE moviesdataset SET RELEASE_YEAR = CONCAT('(', SUBSTRING_INDEX(SUBSTRING_INDEX(RELEASE_YEAR, ') (', -1), ')', 1), ')') WHERE RELEASE_YEAR LIKE '%() (%)%'",
    "UPDATE moviesdataset SET genre = REPLACE(genre, '\n', ''), subgenre = REPLACE(subgenre, '\n', '')",
    "UPDATE moviesdataset SET genre = TRIM(genre), subgenre = TRIM(subgenre)",
    "UPDATE moviesdataset SET Votes = REPLACE(Votes, ',', '')"
]

# Executing UPDATE queries
for query in queries:
    cursor.execute(query)

# Deleting the "gross" column
query = "ALTER TABLE moviesdataset DROP COLUMN GROSS"
cursor.execute(query)

# Committing the changes
connection.commit()

# Executing SQL query to select all rows
query = "SELECT * FROM moviesdataset"
cursor.execute(query)

# Fetching all rows
rows = cursor.fetchall()

# Iterating and processing over each row
for row in rows:
    print(row)