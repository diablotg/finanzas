from django import forms
from .models import TransactionCategory, Transaction


class TransactionCategoryForm(forms.ModelForm):
    class Meta:
        model = TransactionCategory
        fields = ["name"]


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["category", "amount", "transaction_type", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
            "transaction_type": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields["category"].queryset = TransactionCategory.objects.filter(
                user=user
            )

        else:
            self.fields["category"].queryset = TransactionCategory.objects.none()
