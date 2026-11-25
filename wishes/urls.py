from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from wishes import views


urlpatterns = [
    path('wishlists/', views.WishListList.as_view()),
    path('wishlists/<uuid:pk>/', views.WishListDetail.as_view()),
    path('wishes/', views.WishListItems.as_view()),
    path('wishes/<uuid:pk>/', views.WishDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
