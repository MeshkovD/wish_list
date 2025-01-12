from rest_framework import generics

from wishes.models import WishList, Wish
from wishes.serializers import WishSerializer, WishListSerializer


class WishListList(generics.ListCreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class WishListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class WishList(generics.ListCreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer


class WishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
