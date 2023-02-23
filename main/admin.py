from django.contrib import admin
from . import models 
# Register your models here.
admin.site.register(models.booking)

admin.site.register(models.category)
admin.site.register(models.patients)

