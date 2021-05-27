from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]

    fieldsets = (
        (None, {"fields":("username", "password",)}),
        ("personal info", {"fields": ("first_name", "last_name", "email", "phone_number",)})
    )
