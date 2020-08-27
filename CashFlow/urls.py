from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('core/', include('core.urls')),
    path('api/', include('rest_auth.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),

]
