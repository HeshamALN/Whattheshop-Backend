from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Salfa, Cart,CartSalfa


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]


class SalfaInfoSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
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

class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartSalfa
        fields = [
        'cart',
        'salfa',
        ]

class OrderHistorySerializer(serializers.ModelSerializer):
    cart_salfa = AddToCartSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['user','salfa','checkout_status']






class ProfileSerializer(serializers.ModelSerializer):
    carts = OrderHistorySerializer(many=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'carts']

    # def get_history(self, obj):
    #     order = Cart.objects.filter(user=obj.user)
    #     return CartSerializer(order, many=True).data