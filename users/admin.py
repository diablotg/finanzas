from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = (
        "email",
        "full_name",
        "username",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "email",
        "full_name",
        "username",
    )
    ordering = ("username",)

    fieldsets = BaseUserAdmin.fieldsets + (
        ("Información personal", {"fields": ("full_name",)}),
    )


admin.site.register(User, UserAdmin)
