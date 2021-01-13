from django.urls import path
from .views import ExpenseViewSet
from rest_framework.urlpatterns import format_suffix_patterns

expense_detail = ExpenseViewSet.as_view(
    {"get": "retrive", "put": "update", "delete": "destroy", "post": "create"})

expense_list = ExpenseViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = format_suffix_patterns(
    [
        path("expenses/", expense_list),
        path("expenses/<int:pk>", expense_detail),
    ]
)
