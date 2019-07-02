from django.urls import path
from . import views

urlpatterns = [

    # api/restaurant/ (ListView)
    path('restaurant/', views.RestaurantList.as_view(), name='restaurant_list'),
    # api/restaurant/2/ (DetailView)
    path('restaurant/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant_detail'),

    # api/fooditem/ (ListView)
    path('fooditem/', views.FoodItemList.as_view(), name='food_list'),
    # api/fooditem/2/ (DetailView)
    path('fooditem/<int:pk>/', views.FoodItemDetail.as_view(), name='food_detail'),

    # api/order/ (ListView)
    path('order/', views.OrderList.as_view(), name='order_list'),
    # api/order/2/2/ (DetailView)
    path('order/<int:order_restaurant_id>/<int:order_user_id>/', views.OrderUserList.as_view(), name='order_user_list'),

    # api/user/ (ListView)
    path('user/', views.CustomUserList.as_view(), name='user_list'),
    # api/user/2/ (DetailView)
    path('user/<int:pk>/', views.CustomUserDetailById.as_view(), name='user_detail_id'),
    # api/user/admin@admin.com/ (DetailView)
    path('user/<str:user_email_id>/', views.CustomUserDetailByEmail.as_view(), name='user_detail_email'),

    # api/register/
    #path('register/',views.user_register,name='register')

    # api/login/
    #path('login/',views.user_login,name='login')

    # api/forgot_password/
    #path('forgot_password/',views.user_forgot_password,name='forgot_password')

    # api/place_order/
    #path('place_order/',views.user_place_order,name='place_order')
]