from django.contrib import admin
from bloging.models import contactUs
# Register your models here.

admin.site.register(contactUs)



# python manage.py makemigrations
# python manage.py migrate