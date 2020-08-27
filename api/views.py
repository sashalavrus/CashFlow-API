from rest_framework import generics
from costs.models import Expense
from .permissions import IsAuthorOrAdmin

from .serializers import ExpenseSerializer


class ExpenseCreate(generics.CreateAPIView):

    serializer_class = ExpenseSerializer


class ExpenseList(generics.ListCreateAPIView):

    queryset = Expense.objects.all()

    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrAdmin,)

    queryset = Expense.objects.all()

    serializer_class = ExpenseSerializer

