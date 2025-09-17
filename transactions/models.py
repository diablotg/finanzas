from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TransactionCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="General")

    class Meta:
        unique_together = ("name", "user")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    INCOME = "IN"
    EXPENSE = "EX"
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    ]
    transaction_type = models.CharField(
        max_length=7, choices=TRANSACTION_TYPE_CHOICES, default=EXPENSE
    )

    def __str__(self):
        return f"{self.category.name} - {self.amount} - ({self.transaction_type})"
