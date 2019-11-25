from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User as MyUser

# Register your models here.

# Register out own model admin, based on the default UserAdmin
@admin.register(MyUser)
class CustomUserAdmin(UserAdmin):
    pass
