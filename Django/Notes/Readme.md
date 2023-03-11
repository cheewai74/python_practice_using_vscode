Power Shell:
Set-ExecutionPolicy Unrestricted -Scope Process (Administrator)
Set-ExecutionPolicy Unrestricted -Force (Administrator)

python -m venv C:\work\django_ve
python.exe -m pip install --upgrade pip
cd C:\work\django_ve
activate

Impt:
Any changes to model.py: 
1. python manage.py makemigrations
2. python manage.py migrate

HTML & CSS:
https://getbootstrap.com

PIP Install:
pip install Django
pip install stripe

pip install selenium (TDD)
pip install webdriver-manager

pip install pillow (For Django to work with images)
pip install psycopg2 (For Postgres)
pip install django-widget-tweaks
pip  freeze > requirements.txt 

git init
git add -A
git commit -m "First Commit"
heroku create
git push heroku master

Selenium:
copy gecko driver to virtualenv scripts folder


CTRL SHIFT P
Python Interpreter
Click Find...
C:\work\sandbox\Scripts\python.exe


django-admin startproject Django_hello_world

 python manage.py migrate (in outer directory therefore D:\git\python_practice_using_vscode\Django\Django_hello_world\Django_hello_world)

 python manage.py runserver
 python manage.py startapp my_app

 python manage.py migrate
 python manage.py createsuperuser
 username and password: admin12345, admin12345

 python manage.py  makemigrations
 python manage.py migrate

 python manage.py shell

 TDD:
 python manage.py test

 https://passwordsgenerator.net/sha256-hash-generator/