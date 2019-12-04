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


