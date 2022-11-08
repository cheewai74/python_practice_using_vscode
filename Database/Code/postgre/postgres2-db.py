# 
# 1. Create a folder C:\work\postgres-workspace
# 2. python -m venv C:\work\postgres-workspace
# 3. Copy python file to C:\work\postgres-workspace
#
# pip install:
# pip install psycopg2-binary (Note: only works on Python 3.6)
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
# cursor.execute("SELECT * FROM SALES LIMIT 10")
# print(cursor.fetchall())
cursor.execute('''INSERT INTO SALES(ORDER_NUM, 
    ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, 
    QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES
    (1105910, 'Retail', 'Syman Mapstone', 'EB521',
    'Understanding Artificial Intelligence', 3, 19.5,0, 58.5)''')

conn.commit()

cursor.execute("SELECT CUST_NAME, ORDER_TOTAL FROM SALES WHERE ORDER_NUM=1105910")
rows = cursor.fetchall()
for row in rows:
    print("CUST_NAME=", row[0])
    print("ORDER_TOTAL=",row[1],"\n")

conn.close()