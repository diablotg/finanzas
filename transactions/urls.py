from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_transaction, name="create_transaction"),
]
