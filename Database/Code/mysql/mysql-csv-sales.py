import mysql.connector as mysql
import csv

connection = mysql.connect(
    user='root',
    password='',
    host='localhost',
    database='sales',
    allow_local_infile=True)  

# allow_local_infile to true let us read in our csv file locally

cursor=connection.cursor()
    
create_query = '''CREATE TABLE salesperson(
	id INT(255) NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	email_address VARCHAR(255) NOT NULL,
	city VARCHAR(255) NOT NULL,
	state VARCHAR(255) NOT NULL,
	PRIMARY KEY (id))'''
    
cursor.execute("DROP TABLE IF EXISTS salesperson")
cursor.execute(create_query)

# with open('./salespeople.csv', 'r') as f:
# 	csv_data = csv.reader(f)
# 	for row in csv_data:
# 		print(row)
# 		row_tuple = tuple(row)
# 		cursor.execute('INSERT INTO salesperson(first_name, last_name, email_address, city, state) VALUES("%s", "%s", "%s", "%s","%s")', row_tuple)
        
# Path whre you place your csv file in C:\work\mysql-csv-workspace
       
       
# ---------------------------------------------------------------------------------------

q = '''LOAD DATA LOCAL INFILE 
'/work/mysql-csv-workspace/salespeople.csv'
 INTO TABLE salesperson FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
 (first_name, last_name, email_address, city, state);'''


cursor.execute(q)

# ---------------------------------------------------------------------------------------

connection.commit()
cursor.execute("SELECT * FROM salesperson LIMIT 10")
print(cursor.fetchall())
connection.close()