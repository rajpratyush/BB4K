from django.contrib import admin
from .models import KidModel, ParentModel

# Register your models here.

admin.site.register(KidModel)
admin.site.register(ParentModel)