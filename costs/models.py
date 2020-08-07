from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Expense(models.Model):
    """ Class Expense. Contain information about user costs"""

    DEFAULT = 'DF'
    FOOD = 'FD'
    UTILITIES = 'UI'
    TRANSPORT = 'TT'

    CATEGORY_CHOICES = [
        (DEFAULT, 'None'),
        (FOOD, 'Food'),
        (UTILITIES, 'Utilities'),
        (TRANSPORT, 'Transport')
    ]

    amount = models.FloatField(default=0.00)
    category = models.CharField(max_length=2,
                                choices=CATEGORY_CHOICES,
                                default=DEFAULT)
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.amount}, in {self.pub_date}'

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
