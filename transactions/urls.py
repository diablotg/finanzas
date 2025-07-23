from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_transaction, name="create_transaction"),
    path("dashboard/", views.list_transactions, name="dashboard"),
]
