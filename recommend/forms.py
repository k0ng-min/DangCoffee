from django.forms import ModelForm

from recommend.models import Product


class recommendForm(ModelForm):
    class Meta:
        model = Product
        fields = [ 'image', 'name', 'cafe', 'description', 'price', 'digital']