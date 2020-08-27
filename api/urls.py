from django.urls import path
from .views import ExpenseList, ExpenseDetail, ExpenseCreate

app_name = 'api'

urlpatterns = [

    path('expense_create/', ExpenseCreate.as_view(), name='expense_create'),
    path('<int:pk>/', ExpenseDetail.as_view(), ),
    path('expense_list/', ExpenseList.as_view(), name='expense_list'),



]