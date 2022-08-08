from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Menu
from django.db.models import Q
import json

from django.views import View


class MenuView(View):
    def get(self, request):
        menu = list(Menu.objects.values())
        return JsonResponse({'data': menu}, status=200)
