from rest_framework import generics
from rest_framework.exceptions import PermissionDenied

from wishes.models import Wish, WishList
from wishes.serializers import WishListSerializer, WishSerializer


class WishListList(generics.ListCreateAPIView):
    serializer_class = WishListSerializer

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WishListDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WishListSerializer

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)


class WishListItems(generics.ListCreateAPIView):
    serializer_class = WishSerializer

    def get_queryset(self):
        return Wish.objects.filter(wish_list__user=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data['wish_list'].user != self.request.user:
            raise PermissionDenied('Нельзя добавлять желания в чужой список')
        serializer.save()


class WishDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WishSerializer

    def get_queryset(self):
        return Wish.objects.filter(wish_list__user=self.request.user)

    def perform_update(self, serializer):
        if serializer.validated_data.get('wish_list', serializer.instance.wish_list).user != self.request.user:
            raise PermissionDenied('Нельзя переносить желания в чужой список')
        serializer.save()
