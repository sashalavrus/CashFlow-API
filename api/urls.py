from django.urls import path
from .views import ExpenseList, ExpenseDetail


urlpatterns = [

    path('<int:pk>/', ExpenseDetail.as_view()),
    path('', ExpenseList.as_view()),



]