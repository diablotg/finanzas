from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


def home(request):
    return render(request, "users/home.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")

    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("dashboard")  # Redireccionamiento del Dashboard

    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    from django.contrib.auth import logout

    logout(request)
    return redirect(
        "home"
    )  # Redireccionamiento a la página de inicio después de cerrar sesión
