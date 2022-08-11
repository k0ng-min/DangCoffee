from django.db.models.fields import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
from infoapp.models import Menu, Category, Product, Allergy, Image


class MenuView(View):
    def get(self, request):
        menu = list(Menu.objects.values())
        return HttpResponse({'data': menu}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        menu_name = data.get('name', None)

        if not menu_name:
            return HttpResponse({'message': 'KEY_ERROR'}, status=400)

        if Menu.objects.filter(name=data['name']).exists():
            return HttpResponse({'message': 'ALREADY_EXISTS'}, status=409)

        Menu.objects.create(name=menu_name)
        return HttpResponse({'message': 'SUCCESS'}, status=201)


class CategoryView(View):
    def get(self, request):
        category = list(Category.objects.values())
        return HttpResponse({'data':category}, status=200)

    def post(self, request):
        data = json.loads(request.body)

        category_name = data.get('name', None)
        menu_name     = data.get('menu_name', None)

        if not (category_name and menu_name):
            return HttpResponse({'message': 'KEY_ERROR'}, status=400)

        if Category.objects.filter(name=category_name).exists():
            return HttpResponse({'message': 'ALREADY_EXISTS'}, status=409)

        if not Menu.objects.filter(name=menu_name).exists():
            return HttpResponse({'message': 'FOREIGN_KEY_DOES_NOT_EXIST'}, status=404)

        menu = Menu.objects.get(name=menu_name)

        Category.objects.create(
            name=category_name,
            menu=menu
        )
        return HttpResponse({'message': 'SUCCESS'}, status=201)


class ProductView(View):
    def get(self, request):
        product_list = [{
            'id'           : product.id,
            'korean_name'  : product.korean_name,
            'english_name' : product.english_name,
            'description'  : product.description,
            'allergy'      : list(product.allergy.values('name'))
            } for product in Product.objects.all()]
        return HttpResponse({'data':product_list}, status=200)

    def post(self, request):
        data = json.loads(request.body)

        korean_name = data.get('korean_name', None)
        english_name = data.get('english_name', None)
        description = data.get('description', None)
        category_name = data.get('category', None)

        allergy_list = data.get('allergy', None)
        image_list = data.get('image', None)

        if not (korean_name and english_name and description and category_name):
            return HttpResponse({'message': 'KEY_ERROR'}, status=400)

        if not Category.objects.filter(name=category_name).exists():
            return HttpResponse({'message': 'FOREIGN_KEY_DOES_NOT_EXIST'}, status=404)

        category = Category.objects.get(name=data.get('category'))

        product = Product.objects.create(
            korean_name=korean_name,
            english_name=english_name,
            description=description,
            category=category
        )

        if allergy_list:
            for allergy_value in allergy_list:
                allergy = Allergy.objects.get_or_create(name=allergy_value)[0]
                product.allergy.add(allergy)

        if image_list:
            for image in image_list:
                Image.objects.create(
                    image_url=image,
                    product=product
                )

        return HttpResponse({'message': 'SUCCESS'}, status=201)