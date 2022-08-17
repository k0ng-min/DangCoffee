from django.db.models.fields import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View

# Create your views here.


from django.db.models.fields import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
from infoapp.models import Menu, Category, Product, Allergy, Image

from django.shortcuts import render

def productlist(request):
    products = Product.objects.all()
    return render(request, 'infoapp/infolist.html', {'products': products})

def productresult(request):
	query = request.GET['query']
	if query:
		products = Product.objects.filter(korean_name__contains=query)
	return render(request, 'infoapp/result.html', {'products': products})




