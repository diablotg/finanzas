from django.db import models
from users.models import User
from transactions.models import TransactionCategory
from django.utils.translation import gettext_lazy as _


class Budget(models.Model):

    class Month(models.IntegerChoices):
        JAN = 1, _("January")
        FEB = 2, _("February")
        MAR = 3, _("March")
        APR = 4, _("April")
        MAY = 5, _("May")
        JUN = 6, _("June")
        JUL = 7, _("July")
        AUG = 8, _("August")
        SEP = 9, _("September")
        OCT = 10, _("October")
        NOV = 11, _("November")
        DEC = 12, _("December")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.IntegerField(_("Month"), choices=Month.choices)
    year = models.IntegerField(_("Year"))

    def __str__(self):
        month_name = dict(self.Month.choices).get(self.month, "Unknown")
        return f"Budget : {self.user.username} - {self.category.name} - {self.amount} - {month_name} / {self.year}"
