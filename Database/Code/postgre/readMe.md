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

PIP Install:
pip install SQLAlchemy 
pip install psycopg2-binary 

Store Procedure:
1. psql -U postgres
2. \h CREATE PROCEDURE
3. \c red30 - Activate our database

4. CREATE OR REPLACE PROCEDURE return_nondiscounted_item(INT, INT)
5. LANGUAGE plpgsql
6. AS $$
7. BEGIN
8. UPDATE sales
9. SET quantity = quantity -$2, order_total = order_total - price * $2
10. WHERE order_num=$1 AND discount = 0;
11. COMMIT;
12. END;
13. $$; (Note: this $$ will mark the end of the procedure.)

14. SELECT * FROM sales WHERE order_num = 1105910
15. CALL return_nondiscounted_item(1105910, 1);