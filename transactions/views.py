from django.shortcuts import render, redirect
from .forms import TransactionForm


def create_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST, user=request.user)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("home")  # crear una vista de transacciones para redirigir

    else:
        form = TransactionForm(user=request.user)

    return render(request, "transactions/create_transaction.html", {"form": form})
