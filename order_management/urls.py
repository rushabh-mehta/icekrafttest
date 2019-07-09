from django.contrib import admin
from django.urls import path
from . import views

app_name = 'order_management'

urlpatterns = [
    path('login/',views.user_login, name='login'),
    path('active_orders/', views.get_active_orders, name='active_orders'),
    path('update_order/<int:pk>', views.OrderUpdateView.as_view(), name='update_order')
]