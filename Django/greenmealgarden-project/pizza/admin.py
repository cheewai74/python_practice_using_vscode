from django.contrib import admin
from .models import Pizza, Size

# Register your models here.
# Note: Any changes added here: 
#       python manage.py makemigrations
#       python manage.py migrate

admin.site.register(Pizza)
admin.site.register(Size) 
