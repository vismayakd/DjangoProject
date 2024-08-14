from django import forms
from .models import Items

class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']