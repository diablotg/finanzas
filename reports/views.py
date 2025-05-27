from django.shortcuts import render
from transactions.models import Transaction
from budgets.models import Budget
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Sum


@login_required
def monthly_report(request):
    user = request.user
    current_month = datetime.now().month
    current_year = datetime.now().year

    transactions = Transaction.objects.filter(
        user=user, date__month=current_month, date__year=current_year
    )
    total_income = (
        transactions.filter(transaction_type="income").aggregate(total=sum("amount"))[
            "total"
        ]
        or 0
    )
    total_expense = (
        transactions.filter(transaction_type="expense").aggregate(total=sum("amount"))[
            "total"
        ]
        or 0
    )
    total_transactions = total_transactions.count()

    total_balance = total_income - total_expense
    balance_class = "text-success" if total_balance > 0 else "text-danger"

    total_budget = budgets.aggregate(total=Sum("amount"))["total"] or 0
    budget_percent = (
        round((total_balance / total_budget) * 100, 2) if total_budget else 0
    )

    char_labels = [f"{current_month}/{current_year}"]
    char_data = [round(total_expenses + total_income, 2)]

    category_totals = (
        transactions.filter(transaction_type="expense")
        .values("category__name")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )

    category_labels = [cat[category_name] for cat in category_totals]
    category_data = [cat["total"] for cat in category_totals]

    context = {
        "transactions": transactions,
        "budgets": budgets,
        "month": current_month,
        "year": current_year,
        "total_income": round(total_income, 2),
        "total_expense": round(total_expense, 2),
        "total_transactions": total_transactions,
        "total_balance": round(total_balance, 2),
        "balance_class": balance_class,
        "char_labels": char_labels,
        "char_data": char_data,
        "category_labels": category_labels,
        "category_data": category_data,
    }

    return render(request, "reports/monthly_report.html", context)
