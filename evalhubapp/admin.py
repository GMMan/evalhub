from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Evaluator, DaycareUser, SurveyAssignment

# Register your models here.

# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(Evaluator)
admin.site.register(DaycareUser)
admin.site.register(SurveyAssignment)
