from django.contrib import admin

# Register your models here.
from .models import Users,Assets
admin.site.register(Users)
admin.site.register(Assets)