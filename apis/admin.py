from django.contrib import admin
from .views import CustomUser, FoodItem, Restaurant, Order, OrderFoodItem
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.unregister(Group)

admin.site.register(CustomUser)
admin.site.register(FoodItem)
admin.site.register(Restaurant)
admin.site.register(OrderFoodItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order_created_on', 'order_updated_on', 'order_table_number', 'order_active', 'order_total_amount', 'order_confirm')
    list_filter = ('order_active', 'order_confirm','order_created_on','order_updated_on')
    list_editable = ( 'order_table_number','order_total_amount','order_active','order_confirm')
    list_display_links = ['pk']
    search_fields = ['order_created_on','order_updated_on']
    




