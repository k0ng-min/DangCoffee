# Create your views here.
from django.shortcuts import render

def Suggest(request):
    return render(request, 'recommendapp/suggest.html')