initdb -D C:\work\postgreSQL

cd C:\work\postgreSQL


psql -U postgres
\list
CREATE DATABASE red30;
\list 

<!-- To connect to database red30 -->
\c red30 

C:\work\postgres-workspace

<!-- Enter postgres  -->
\copy sales FROM 'C:\work\postgres-workspace\red30-postgres.csv' WITH DELIMITER ',' CSV HEADER;

pip install SQLAlchemy 
