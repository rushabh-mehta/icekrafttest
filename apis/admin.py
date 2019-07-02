from django.contrib import admin
from .views import CustomUser, FoodItem, Restaurant, Order


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(FoodItem)
admin.site.register(Restaurant)
admin.site.register(Order)