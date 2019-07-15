from apis.models import Order, FoodItem
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

class OrderForm(BSModalForm):

    class Meta:
        model = Order
        fields = ['order_confirm','order_active']

class FoodItemForm(BSModalForm):
    class Meta:
        model = FoodItem
        fields = ['fooditem_name', 'fooditem_cost', 'fooditem_description', 'fooditem_picture']

