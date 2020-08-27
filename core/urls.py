from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from core.views import CreateUserView

app_name = 'core'

urlpatterns = [

    path('signup/', CreateUserView.as_view(), name='signup'),
    path('token/', obtain_auth_token, name='token'),
]