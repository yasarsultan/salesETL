import psycopg2
from psycopg2 import sql

# Establishing connection
def create_connection():
    connection = psycopg2.connect(
        dbname="sales_db",
        user="practitioner",
        password="admin123",
        host="localhost",
        port="5432"
    )
    connection.autocommit = True
    return connection

# Creating a database if it doesn't already exist
def create_database(connection):
    cur = connection.cursor()
    try:
        cur.execute("CREATE DATABASE sales_db")
    except:
        print("Database 'sales_db' already exists")

# Creating table based on given parameters if it doesn't already exist
def create_table(connection, table_name, table_schema):
    cur = connection.cursor()
    cur.execute(
        sql.SQL('CREATE TABLE IF NOT EXISTS {} ({})').format(
            sql.Identifier(table_name),
            sql.SQL(table_schema)
        )
    )
    
# Inserting data into specified table
def insert_data(connection, table_name, dataframe):
    cur = connection.cursor()
    for _, row in dataframe.iterrows():
        cur.execute(
            sql.SQL("INSERT INTO {}  VALUES ({})").format(
                sql.Identifier(table_name),
                sql.SQL(', ').join(sql.Placeholder() * len(row))
            ),
            tuple(row)
        )

# Closing the connection
def close_connection(connection):
    connection.close()

product_structure = """
product_id VARCHAR(100),
product_name TEXT,
category TEXT,
discounted_price TEXT,
actual_price TEXT,
distcounted_percentage TEXT,
rating TEXT,
rating_count TEXT,
about_product TEXT,
img_link TEXT,
product_link TEXT
"""

review_structure = """
product_id VARCHAR(100),
review_id VARCHAR(255),
review_title TEXT,
review_content TEXT,
negative_score INT,
neutral_score INT,
positive_score INT,
compound_score INT
"""

user_structure = """
product_id VARCHAR(100),
user_id VARCHAR(100),
user_name VARCHAR(100)
"""