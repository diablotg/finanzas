from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("users/", include("users.urls")),
    path("reports/", include("reports.urls")),
]
