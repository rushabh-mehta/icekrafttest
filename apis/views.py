from django.shortcuts import render,HttpResponseRedirect
from rest_framework import generics
from .models import Restaurant, FoodItem, Order, CustomUser, OrderFoodItem
from .serializers import RestaurantSerializer, FoodItemSerializer,OrderSerializer, CustomUserSerializer, OrderFoodItemSerializer
import requests
import json
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
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

class OrderFoodItemList(generics.ListAPIView):

    def get_queryset(self):
        order_id = self.kwargs['orderfooditem_order_id']
        order_object = Order.objects.get(pk=order_id)
        return order_object.orderfooditem_set.all()

    serializer_class = OrderFoodItemSerializer
class UserActiveOrder(generics.ListAPIView):

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Order.objects.filter(order_user_id = user_id,order_active=True)
        
    serializer_class = OrderSerializer

@csrf_exempt
def place_order(request):
    '''Places an order based on the POST request from the front-end.
        Extracts data from the body of the request which is in json.
        Parses the json to get the individual elements.
        Creates a new object of the Order model with the obtained data.
        Then loops through the fooditems in the order and establishes many to many relationship between the
        Order object created and the specificied FoodItems'''
    
    # Check for a POST request and extract information from the json
    if request.method == "POST":
        received_json_data=json.loads(request.body)

        user_id = received_json_data['order_user_id']
        user_object = CustomUser.objects.get(pk=user_id)
        restaurant_id = received_json_data['order_restaurant_id']
        restaurant_object = Restaurant.objects.get(pk=restaurant_id)
        table_number = received_json_data['order_table_number']
        active = True
        total_amount = received_json_data['order_total_amount']
        confirm = False

        food_items_user_selected = received_json_data['order_food_item_selected']
        food_quantities = received_json_data['order_food_quantities']
        #string_food_quantities = ",".join(repr(quantity) for quantity in food_quantities)

        # Create a new order
        order_object = Order(order_user_id=user_object, order_restaurant_id=restaurant_object ,order_table_number=table_number,
        order_active=active , order_total_amount=total_amount , order_confirm=confirm)
        order_object.save()

        # Add the relation between fooditems the user selected and the order object created above also calculate the total order bill.

        # total_amount = 0
        counter = 0
        for food in food_items_user_selected:
            fooditem_object = FoodItem.objects.get(pk=int(food))
            food_quantity = food_quantities[counter]
            #order_object.order_fooditem_relation.add(fooditem_object)
            #total_amount+= fooditem_object.fooditem_cost*food_quantity
            OrderFoodItem.objects.create(orderfooditem_order_id=order_object, orderfooditem_fooditem_id=fooditem_object, orderfooditem_quantity=food_quantity, orderfooditem_fooditem_name = fooditem_object.fooditem_name)
            counter+=1
        
        # Add the total bill to the order object created above.
        # order_object.order_total_amount = total_amount
        order_object.save()
        return render(request,'order_management/place_order_successful.html')
 



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

