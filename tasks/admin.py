# zentodo_backend/tasks/admin.py

from django.contrib import admin
from .models import Todo # Import your Todo model

# Register your models here.
admin.site.register(Todo)