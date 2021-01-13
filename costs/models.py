from djongo import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Expense(models.Model):
    """ Class Expense. Contain information about user costs"""

    amount = models.FloatField(default=0.00)
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.amount}, in {self.pub_date}'

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
