from django.shortcuts import render, redirect
from .models import TransactionCategory, Transaction
from .forms import TransactionCategoryForm, TransactionForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    transaction_form = TransactionForm(user=request.user)
    category_form = TransactionCategoryForm()

    if request.method == "POST":
        if "transaction_submit" in request.POST:
            transaction_form = TransactionForm(request.POST, user=request.user)
            if transaction_form.is_valid():
                transaction = transaction_form.save(commit=False)
                transaction.user = request.user
                transaction.save()
                return redirect("dashboard")

        elif "category_submit" in request.POST:
            category_form = TransactionCategoryForm(request.POST)
            if category_form.is_valid():
                category = category_form.save(commit=False)
                category.user = request.user
                category.save()
                return redirect("dashboard")

    transactions = Transaction.objects.filter(user=request.user)
    categories = TransactionCategory.objects.filter(user=request.user)

    context = {
        "transaction_form": transaction_form,
        "category_form": category_form,
        "transactions": transactions,
        "categories": categories,
    }
    return render(request, "transactions/dashboard.html", context)
