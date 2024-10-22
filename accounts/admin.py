from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Subject, Schedule

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("schedule",)}),(None, {"fields": ("subjects",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("schedule",)}),(None, {"fields": ("subjects",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subject)
admin.site.register(Schedule)
