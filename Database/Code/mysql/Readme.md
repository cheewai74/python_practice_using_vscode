XAMPP:
mysql -h localhost -u root

Cmder:
CREATE DATABASE projects;

create mysql-workspace folder
python -m venv C:\work\mysql-workspace
cd C:\work\mysql-workspace\scripts
activate
pip install mysql-connector-python

Copy mysql-database.py to mysql-workspace folder
At virtual environment, python mysql-database.py

// -----------------------------------------------------------//

create mysql-sqlalchemy-workspace folder
python -m venv C:\work\mysql-sqlalchemy-workspace

cd C:\work\mysql-sqlalchemy-workspace

pip install mysql-connector-python
pip install SQLAlchemy 
