from django.db import models
from django.core.validators import RegexValidator, int_list_validator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    '''Overrides the custom django user model'''

    # Datafields
    NORMAL_USER = 1
    RESTAURANT_1_ADMIN = 2
    RESTAURANT_2_ADMIN = 3
    RESTAURANT_3_ADMIN = 4
    RESTAURANT_4_ADMIN = 5
    RESTAURANT_5_ADMIN = 6
    RESTAURANT_6_ADMIN = 7
    RESTAURANT_7_ADMIN = 8
    RESTAURANT_8_ADMIN = 9
    RESTAURANT_9_ADMIN = 10
    RESTAURANT_10_ADMIN = 11
    RESTAURANT_11_ADMIN = 12
    SUPER_ADMIN = 13
    ROLE_CHOICES = (
      (NORMAL_USER,'normal_user'),
      (RESTAURANT_1_ADMIN,'restaurant_1_admin'),
      (RESTAURANT_2_ADMIN,'restaurant_2_admin'),
      (RESTAURANT_3_ADMIN,'restaurant_3_admin'),
      (RESTAURANT_4_ADMIN,'restaurant_4_admin'),
      (RESTAURANT_5_ADMIN,'restaurant_5_admin'),
      (RESTAURANT_6_ADMIN,'restaurant_6_admin'),
      (RESTAURANT_7_ADMIN,'restaurant_7_admin'),
      (RESTAURANT_8_ADMIN,'restaurant_8_admin'),
      (RESTAURANT_9_ADMIN,'restaurant_9_admin'),
      (RESTAURANT_10_ADMIN,'restaurant_10_admin'),
      (RESTAURANT_11_ADMIN,'restaurant_11_admin'),
      (SUPER_ADMIN,'super_admin'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=NORMAL_USER)
    user_reward_points = models.FloatField(default=0)


class FoodItem(models.Model):
    #Datafields
    fooditem_name = models.CharField(max_length = 500)
    fooditem_cost = models.FloatField()
    fooditem_description = models.CharField(max_length = 1000)
    fooditem_picture = models.FileField()
    
    def __str__(self):
        return self.fooditem_name

class Restaurant(models.Model):
    ''' This model has a many to many relation with the food-items, this relation can be used to build the menu
        for each restaurant'''

    #Relationships
    restaurant_fooditem_relation = models.ManyToManyField(FoodItem)

    #Datafields
    restaurant_name = models.CharField(max_length=300)
    restaurant_address = models.CharField(max_length = 1000)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number is not valid!")
    restaurant_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 

    def __str__(self):
        return self.restaurant_name


class Order(models.Model):
    '''This model has a one to many relation with user and restaurant. This model has many to many relation with fooditems. '''

    #Relationships
    order_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_fooditem_relation = models.ManyToManyField(FoodItem, through="OrderFoodItem")
    
    #Datafields
    order_created_on = models.DateTimeField(auto_now_add=True)
    order_updated_on = models.DateTimeField(auto_now=True)
    order_table_number = models.IntegerField()
    order_active = models.BooleanField()
    order_total_amount = models.FloatField()
    order_confirm = models.BooleanField()
    
    # quantity_regex = int_list_validator(sep=",",allow_negative=False)
    # order_quantity = models.CharField(validators=[quantity_regex], max_length=500, blank=True)

    def __str__(self):
        return str(self.order_created_on)+" "+str(self.order_restaurant_id)+" "+str(self.order_table_number)+" "+str(self.order_active)
    

class OrderFoodItem(models.Model):
    
    orderfooditem_order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    orderfooditem_fooditem_id = models.ForeignKey(FoodItem,on_delete=models.CASCADE,  related_name="orderfooditem_fooditem_id")
    orderfooditem_fooditem_name = models.CharField(max_length = 500, blank=True)
    orderfooditem_quantity = models.IntegerField()


    def __str__(self):
        return str(self.orderfooditem_fooditem_id)+" "+str(self.orderfooditem_quantity)