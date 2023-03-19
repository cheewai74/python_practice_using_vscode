
Virtual Environment:
py -m venv venv
venv\Scripts\activate

PIP Install:
pip install flask
pip install flask-wtf
pip install python-dotenv
pip install flask-mongoengine
pip install flask-wtf flask-security
pip list

create a file ".flaskenv"

pip freeze > requirements.txt
pip install -r requirements.txt

Create a ".flaskenv" file.
Create a file main.py
Create a config.py
Create a routes.py file in Application folder.


flask commands:
flask run

mongo --version