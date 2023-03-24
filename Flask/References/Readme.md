
Virtual Environment:
py -m venv venv
venv\Scripts\activate

PIP Install:
pip install wheel
pip install flask
pip install flask-wtf
pip install python-dotenv
pip install flask-mongoengine
pip install flask-wtf flask-security
pip install flask-restplus

pip install Flask-SQLAlchemy (For SQLLite)
pip install flask-marshmallow
pip install marshmallow-sqlalchemy

pip install Flask-Login
pip install Flask-User
pip install Flask-JWT-Extended
pip install Flask-Mail
pip list

create a file ".flaskenv"

pip freeze > requirements.txt
pip install -r requirements.txt

Create a ".flaskenv" file.
Create a file main.py
Create a config.py
Create a routes.py file in Application folder.


flask commands:
flask db_create (Referred to app.py on planetary-api)
flask db_seed (Referred to app.py on planetary-api)
flask run


mongo --version