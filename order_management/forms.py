from apis.models import Order
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

class OrderForm(BSModalForm):

    class Meta:
        model = Order
        fields = ['order_confirm','order_active']

