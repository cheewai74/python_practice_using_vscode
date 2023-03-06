1. django-admin startproject #project_name
2. django-admin startapp #apps_name
3. Rename #project_name to #project_name-project
4. "python manage.py runserver" to check if it's working, CTRL +C to quit.
5. At setting.py in #apps_name folder, look for INSTALLED_APPS = [ ..] and add
   '#apps_name'
6. Create 2 folders in #app_name folder
   6.1 templates
   6.2 templates/#app_name
   6.3 Create a html and place it in templates/#app_name folder. E.g: nick.html (content Hello World!)
7. #app_name/urls.py
   7.1. Add import #apps_name.views E.g: import jobs.views.
   7.2. Add a path E.g: path('nick', jobs.views.nick, name='nick'),
8. Create a view method in #app_name/views.py
   def nick(request):
      return render(request, 'jobs/nick.html')
9. Referred to Optional steps, Database
10. python manage.py makemigrations
11. python manage.py migrate
12. Create an admin account
    - python manage.py createsuperuser 
    - E.g: username: nick password: django1234
13. #app_name folder > admin.py
    - from .model import #class_name (Referred to #app_name/models.py E.g Job)
    - admin.site.register(#class_name)
14. #app_name folder > views.py
    - from .model import #class_name (Referred to #app_name/models.py E.g Job)
15. Create a folder "static" in #app_name folder
16. #app_name folder > settings.py
   - look for STATIC_URL = 'static/'
   E.g: add STATIC_ROOT = os.path.join(BASE_DIR, 'static')
17. #app_name/urls.py
    - from django.conf import settings
    - from django.conf.urls.static import static
    - urlpatterns = [...] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
18. python manage.py collectstatic
19. home.html
    -  {% load static %} 

Optional

Database:
   Note: pip install psycopg2 (For Postgres)
   #project_name folder > Setting.py 
   DATABASES = {..}