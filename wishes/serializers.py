from rest_framework import serializers

from wishes.models import WishList, Wish


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'
