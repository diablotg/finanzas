from django.contrib import admin
from django.urls import path, include
from users.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Página de inicio
    path("reports/", include("reports.urls")),
]
