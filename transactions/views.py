from django.shortcuts import render, redirect
from .models import TransactionCategory, Transaction
from .forms import TransactionCategoryForm, TransactionForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def dashboard(request):
    transaction_form = TransactionForm(user=request.user)
    category_form = TransactionCategoryForm(user=request.user)

    if request.method == "POST":
        if "transaction_submit" in request.POST:
            transaction_form = TransactionForm(request.POST, user=request.user)
            if transaction_form.is_valid():
                transaction = transaction_form.save(commit=False)
                transaction.user = request.user
                transaction.save()
                return redirect("dashboard")

        elif "category_submit" in request.POST:
            category_form = TransactionCategoryForm(request.POST, user=request.user)
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


@login_required
def delete_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    transaction.delete()
    return redirect("dashboard")


@login_required
def delete_category(request, id):
    category = get_object_or_404(TransactionCategory, id=id, user=request.user)
    category.delete()
    return redirect("dashboard")
