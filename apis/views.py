from django.shortcuts import render,HttpResponseRedirect
from rest_framework import generics
from .models import Restaurant, FoodItem, Order, CustomUser
from .serializers import RestaurantSerializer, FoodItemSerializer,OrderSerializer, CustomUserSerializer
import requests
import json
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

class RestaurantList(generics.ListAPIView):
    '''ListView for the api endpoint /api/restaurant/'''
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveAPIView):
    '''DetailView for the api endpoint /api/restaurant/2/'''
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class FoodItemList(generics.ListAPIView):
    '''ListView for the api endpoint /api/fooditem/'''
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class FoodItemDetail(generics.RetrieveAPIView):
    '''DetailView for the api endpoint /api/fooditem/2/'''
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class OrderList(generics.ListAPIView):
    '''ListView for the api endpoint /api/order/'''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUserList(generics.ListAPIView):
    '''DetailView for the api endpoint /api/order/2/2/'''

    # Gets the list of orders a particular user makes in a particular restaurant.
    def get_queryset(self):
        user_id = self.kwargs['order_user_id']
        restaurant_id = self.kwargs['order_restaurant_id']
        return Order.objects.filter(order_user_id=user_id, order_restaurant_id=restaurant_id)

    serializer_class = OrderSerializer


class CustomUserList(generics.ListAPIView):
    '''ListView for the api endpoint /api/user/'''
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailById(generics.RetrieveAPIView):
    '''DetailView for the api endpoint /api/user/2/'''
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailByEmail(generics.ListAPIView):
    '''DetailView for the api endpoint /api/user/admin@admin.com/'''
    
    #Gets the queryset of a particular user by email-id.
    def get_queryset(self):
        email_id = self.kwargs['user_email_id']
        return CustomUser.objects.filter(email=email_id)
        
    serializer_class = CustomUserSerializer


""" def place_order(request):
    '''Places an order based on the POST request from the front-end.
        Extracts data from the body of the request which is in json.
        Parses the json to get the individual elements.
        Creates a new object of the Order model with the obtained data.
        Then loops through the fooditems in the order and establishes many to many relationship between the
        Order object created and the specificied FoodItems'''
    
    # Check for a POST request and extract information from the json
    if request.POST:
        received_json_data=json.loads(request.body)

        user_id = 
        user_object = CustomUser.objects.get(pk=user_id)
        restaurant_id = 
        restaurant_object = Restaurant.objects.get(pk=restaurant_id)
        created_on = 
        updated_on = 
        table_number = 
        active = 
        total_amount = 
        confirm = 

        food_items_user_selected = 

        # Create a new order
        order_object = Order(order_user_id =, order_restaurant_id = , order_created_on = , order_updated_on = , 
                            order_table_number = , order_active = , order_total_amount = , order_confirm = )
        order_object.save()

        # Add the relation between fooditems the user selected and the order object created above also calculate the total order bill.
        total_amount = 0
        for food in food_items_user_selected:
            fooditem = FoodItem.objects.get(pk=food)
            order_object.order_fooditem_relation.add(fooditem)
            total_amount+= fooditem.fooditem_cost
        
        # Add the total bill to the order object created above.
        order_object.order_total_amount = total_amount
        order_object.save() """


""" def user_register(request):
    registered = False
    username = 'admin1'  # changes here
    password = 'admin1'  # changes here
    if request.POST:
        if CustomUser.objects.filter(username = username).exists():
            return False # changes here
        else:
            user = CustomUser.objects.create(username=username, password= password,role=1) # changes here.
            login(request, user)
            return HttpResponseRedirect(reverse('user_list'))   # changes here
 """

""" def user_login(request):
    if request.POST:
        username = 'admin'  # changes here
        password = 'admin'  # changes here
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('user_list'))   # changes here
        else:
            return HttpResponseRedirect(reverse('restaurant_list')) """

""" def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('restaurant_list')) # changes here """

""" def user_forgot_password(request):
    pass """


