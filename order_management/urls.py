from django.contrib import admin
from django.urls import path
from . import views

app_name = 'order_management'

urlpatterns = [
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('active_orders/', views.get_active_orders, name='active_orders'),
    path('past_orders/', views.get_past_orders, name='past_orders'),
    path('update_order/<int:pk>', views.OrderUpdateView.as_view(), name='update_order'),
    path('delete_order/<int:pk>', views.OrderDeleteView.as_view(), name='delete_order'),
    path('menu/', views.get_restaurant_menu, name="restaurant_menu"),

    path('create_restaurant_menu/', views.RestaurantMenuCreateView.as_view(), name='create_restaurant_menu'),
    path('update_restaurant_menu/<int:pk>', views.RestaurantMenuUpdateView.as_view(), name='update_restaurant_menu'),
    path('delete_restaurant_menu/<int:pk>', views.RestaurantMenuDeleteView.as_view(), name='delete_restaurant_menu'),
]