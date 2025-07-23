from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction, TransactionCategory
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_default_category(sender, instance, created, **kwargs):
    if created:
        default_categories = [
            "Food",
            "Transport",
            "Entertainment",
            "Utilities",
            "Health",
            "Education",
            "Shopping",
            "Other",
        ]
        for category_name in default_categories:
            TransactionCategory.objects.get_or_create(user=instance, name=category_name)
