from rest_framework import serializers
from . import models


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = '__all__'



class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FoodItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = '__all__'



class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = '__all__'