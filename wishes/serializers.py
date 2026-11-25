from rest_framework import serializers

from wishes.models import Wish, WishList


class WishListSerializer(serializers.ModelSerializer):
    wishes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = WishList
        fields = ['uuid', 'wishes', 'created_at', 'updated_at']


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ['uuid', 'wish_list', 'product', 'created_at', 'updated_at']
