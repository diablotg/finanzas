from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = (
        "email",
        "first_name",
        "last_name",
        "username",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "email",
        "username",
    )
    ordering = ("username",)


admin.site.register(User, UserAdmin)
