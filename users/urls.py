from django.urls import path
from .views import home
from .views import register

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
]
