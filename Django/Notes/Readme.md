Power Shell:
Set-ExecutionPolicy Unrestricted -Scope Process (Administrator)
Set-ExecutionPolicy Unrestricted -Force (Administrator)

python -m venv C:\work\django_ve
python.exe -m pip install --upgrade pip
cd C:\work\django_ve
activate

pip install Django
pip install pillow (For Django to work with images)

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