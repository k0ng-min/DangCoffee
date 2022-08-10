from django.forms import ModelForm

from infoapp.models import Product


class recommendForm(ModelForm):
    class Meta:
        model = Product
        fields = [ 'image', 'menu', 'category', 'product', 'AllergyProduct', 'Nutrition']