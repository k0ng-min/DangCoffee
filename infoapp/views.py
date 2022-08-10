from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

import infoapp.models


def MainSearch(request) :
    return render(request, 'info/list.html')

class ProductListView(ListView):
    model = infoapp.models.Product
    context_object_name = 'product_list'
    template_name = 'infoapp/list.html'
    paginate_by = 10