from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm


def home(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(
                request, user
            )  # Iniciar sesión automáticamente después de registrarse
            return redirect(
                "home"
            )  # Redirigir a la página principal o a donde lo necesites
    else:
        form = UserRegistrationForm()

    return render(request, "home.html", {"form": form})
