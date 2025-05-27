from django.urls import path
from . import views

urlpatterns = [
    path("monthly-report/", views.monthly_report, name="monthly_report"),
]
