from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.db import models


userfields = list(UserAdmin.fieldsets)
userfields[1] = ('Личная информация', {'fields': ('first_name', 'last_name', 'email', 'mobilephone')})
UserAdmin.fieldsets = tuple(userfields)

admin.site.register(Cat)
admin.site.register(NewUser, UserAdmin)
