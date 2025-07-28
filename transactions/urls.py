from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_transaction, name="create"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("list/", views.list_transactions, name="list_transactions"),
    path("category/", views.create_category, name="category"),
]
