from django.http import request
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


def searchresult(request):
    if ('keyword' in request.GET) and ('cafe[]' and 'drink[]' in request.POST):
        query = request.GET('keyword' and 'cafe[]' and 'drink')

        products = Product.objects.all().filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(cafe__icontains=query) |
            Q(category__icontains=query)
        )
        # PRODUCT에서 filter를 통해 검사
        # __icontains로 name 안에 query와 동일한 값이 있는지 대소문자 상관없이 검색

        return render(request, 'recommend/recommend2.html', {'query': query, 'products': products})

    # 검색결과로 query랑 products 리턴


def input_test(request):
    if request.POST:
        list_item = request.POST.getlist('test')
        print(list_item)
