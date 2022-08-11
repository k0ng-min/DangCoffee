from django.forms import ModelForm

from infoapp.models import Product


class infoForm(ModelForm):
    class Meta:
        model = Product
        fields = [ 'image', 'menu', 'category', 'product', 'AllergyProduct', 'Nutrition']