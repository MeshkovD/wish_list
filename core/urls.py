from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('wishes.urls')),
]
