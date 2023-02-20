from django.forms import ModelForm
from .models import ManufacturedProduct, Product


class ManufacturedProductForm(ModelForm):
    class Meta:
        model = ManufacturedProduct
        fields = ['product', 'amount', 'measure', 'unit_price', 'code', 'description']
