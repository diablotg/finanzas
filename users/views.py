from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import logout


def home(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("create_transaction")
        else:
            messages.error(request, "Credenciales incorrectas.")
    else:
        form = AuthenticationForm()
    return render(request, "users/home.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {"form": form})
