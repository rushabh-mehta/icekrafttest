from django.shortcuts import render
from apis.models import CustomUser, FoodItem, Restaurant, Order, OrderFoodItem
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def user_login(request):
    if request.method == "POST":
        username =  request.POST['username'] # changes here
        password = request.POST['password']  # changes here
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('order_management:active_orders'))   
        else:
            return render(request, 'order_management/login.html',{'error_message': 'Username or Password Incorrect!'})
            #return HttpResponseRedirect(reverse('order_management:login'))

    else:
        return render(request, 'order_management/login.html')

def get_active_orders(request):
    user_role = 1
    active_orders = Order.objects.filter(order_restaurant_id=user_role, order_active=True)
    food_items_in_order = []
    for order in active_orders:
        food_items_in_order.append(OrderFoodItem.objects.filter(orderfooditem_order_id=order))
    data = {'order_data':active_orders,'food_data':food_items_in_order}
    return render(request, 'order_management/active_orders.html',data)