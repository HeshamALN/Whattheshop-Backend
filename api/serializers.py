from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Salfa, Cart,CartSalfa


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data



class SalfaCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salfa
        fields = [
        'name',
        'type',
        'owner',
        'description',
        'price',
        'img',
            ]


class SalfaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salfa
        fields = [
        'id', 
        'name',
        'type',
        'owner',
        'description',
        'price',
        'img',

        ]

class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartSalfa
        fields = [
        'cart',
        'salfa',
        ]


# class CartSerializer(serializers.ModelSerializer):
#     total_price = serializers.SerializerMethodField()
#     class Meta:
#         model = Cart
#         fields = [
#         'id',
#         'name',
#         'type',
#         'price',
#         'img','total_price'
#         ]

#     def get_total_price(self,obj):
#         total =0
#         for bought in obj.salfa.all():
#             prices = bought.price
#             total += prices
#         return total

