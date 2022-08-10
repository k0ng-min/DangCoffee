from django.shortcuts import render
from .models import Product
from django.db.models import Q


# Q함수를 통해 상품의 이름이나 설명을 OR이나 AND 조건으로 데이터 검색 가능


def home(request):
    return render(request, 'base.html')


def recommend1(request):
    return render(request, 'recommend/recommend1.html')


def recommend2(request):
    return render(request, 'recommend/recommend2.html')


def search(request, priceRangeMin=None, priceRangeMax=None):
    if 'keyword' in request.GET:
        query = request.GET.get('keyword')

        products = Product.objects.all().filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(cafe__icontains=query)
        )

    if request.method=="POST":

        if 'cafe' and 'drink' and 'priceRangeMin' and 'priceRangeMax' in request.POST:
            saved = Product()
            saved.cafe = request.POST.getlist('cafe')
            saved.category = request.POST.getlist('drink')
            query = saved.cafe and saved.category

            products = Product.objects.all().filter(
                Q(cafe=saved.cafe) &
                Q(category=saved.category) &
                (priceRangeMin <= products.price <= priceRangeMax)
            )

    return render(request, 'recommend/recommend2.html', {'query': query, 'products': products})



def input_test(request):
    if request.POST:
        list_item = request.POST.getlist('test')
        print(list_item)