from django import forms
from core.models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['order_first_name', 'order_last_name', 'order_cc_no', 'order_cc_date', 'order_address']

