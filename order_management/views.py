from django.shortcuts import render
from apis.models import CustomUser, FoodItem, Restaurant, Order, OrderFoodItem
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import OrderForm
from bootstrap_modal_forms.generic import BSModalUpdateView
# Create your views here.

class OrderUpdateView(BSModalUpdateView):
    model = Order
    template_name = 'order_management/update_order.html'
    form_class = OrderForm
    success_message = 'Order Updated!'
    success_url = reverse_lazy('order_management:active_orders')


def user_login(request):
    """Logs in a user if the credentials are valid and the user is active, else redirects to the same page and displays an error message."""
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
    """Takes the role of the current logged in user & accordgin to the role gets the active orders. User role 
    signifies the restaurant of which they are the admin.
    After the active orders are fetched, we loop through each of the orders and get the corresponding fooditems
    in that order.
    Then we loop through the fooditems and create a dictionary where the key is the fooditem name & the value is 
    the fooditem quantity.
    We loop through each of the orders which gives us a list of such dictionaries.
    Then the order data & the corresponding food items data is zipped together and passed to the template."""

    # User role of current logged in user.
    user_role = request.user.role-1
    # List of order objects which are active.
    active_orders = Order.objects.filter(order_restaurant_id=user_role, order_active=True)
    food_items_in_order = []

    for order in active_orders:
        # List of orderfooditem objects which are part of the specific order.
        food_items = OrderFoodItem.objects.filter(orderfooditem_order_id=order)
        food_items_dict = {}
        for food_item in food_items:
            # Name of the fooditem in the fooditem list
            fooditem_name =  food_item.orderfooditem_fooditem_id.fooditem_name
            # A dictionary of fooditems where the fooditem name is key & the fooditem quantitiy is value.
            food_items_dict[fooditem_name]=food_item.orderfooditem_quantity

        # Appending the dictionary to the list which contains such fooditem dictionaries for all orders.
        food_items_in_order.append(food_items_dict)
     # Zipping the order data & the fooditem data of the corresponding order together.   
    order_data = zip(active_orders,food_items_in_order)
    data = {'order_data':order_data,'user_role':user_role}
    return render(request, 'order_management/active_orders.html',data)