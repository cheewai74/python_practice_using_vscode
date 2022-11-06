# 
# 1. Create a folder C:\work\postgres-workspace
# 2. python -m venv C:\work\postgres-workspace
# 3. Copy python file to C:\work\postgres-workspace
#
# pip install:
# pip install psycopg2
# pip install psycopg2-binary
#
# Execute:
# deactivate python virtual environment
# psql -U postgres
# \c red30
# \dt


import psycopg2
conn = psycopg2.connect(database="red30",
	user="postgres",
	password="password",
	host="localhost",
	port="5432")


cursor = conn.cursor()

cursor.execute('''CREATE TABLE Sales
    (ORDER_NUM INT PRIMARY KEY,
        ORDER_TYPE TEXT,
        CUST_NAME TEXT,
        PROD_NUMBER TEXT,
        PROD_NAME TEXT,
        QUANTITY INT,
        PRICE REAL,
        DISCOUNT REAL,
        ORDER_TOTAL REAL);''')

conn.commit()
conn.close()