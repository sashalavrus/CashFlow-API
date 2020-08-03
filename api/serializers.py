from rest_framework import serializers
from costs.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('author', 'amount', 'category', 'pub_date')