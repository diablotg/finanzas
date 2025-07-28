from django.shortcuts import render, redirect
from .forms import TransactionForm
from .forms import TransactionCategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError


@login_required
def dashboard(request):
    transactions = request.user.transaction_set.all().order_by("-date")
    categories = request.user.transactioncategory_set.all()

    return render(
        request,
        "transactions/dashboard.html",
        {
            "transactions": transactions,
            "categories": categories,
        },
    )


@login_required
def create_category(request):
    if request.method == "POST":
        form = TransactionCategoryForm(request.POST, user=request.user)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user

            try:
                category.save()
                messages.success(
                    request, f'Category: "{category.name}" created successfully!'
                )
                return redirect("category")
            except IntegrityError:
                form.add_error("name", "This category already exists for your account.")
    else:
        form = TransactionCategoryForm(user=request.user)

    categories = request.user.transactioncategory_set.all()

    return render(
        request,
        "transactions/create_category.html",
        {
            "form": form,
            "categories": categories,
        },
    )


@login_required
def create_transaction(request):
    if request.method == "POST":
        category_form = TransactionCategoryForm(request.POST, user=request.user)
        transaction_form = TransactionForm(request.POST, user=request.user)

        if category_form.is_valid() and transaction_form.is_valid():
            category_form.save()
            transaction = transaction_form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("create")
    else:
        category_form = TransactionCategoryForm(user=request.user)
        transaction_form = TransactionForm(user=request.user)

    return render(
        request,
        "transactions/create_transaction.html",
        {
            "category_form": category_form,
            "transaction_form": transaction_form,
        },
    )


@login_required
def list_transactions(request):
    transactions = request.user.transaction_set.all().order_by("-date")
    categories = request.user.transactioncategory_set.all()

    return render(
        request,
        "transactions/list_transactions.html",
        {
            "transactions": transactions,
            "categories": categories,
        },
    )
