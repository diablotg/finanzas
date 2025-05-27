from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm


def home(request):
    return render(request, "users/home.html")


def register(request):
    return render(request, "users/register.html")
