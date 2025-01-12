from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views


urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<uuid:pk>/', views.CustomUserDetail.as_view()),

    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<uuid:pk>/', views.ProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
