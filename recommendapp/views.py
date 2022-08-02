from django.shortcuts import render

# Create your views here.


def Suggest(request):
    return render(request, 'recommendapp/suggest.html')