from django.shortcuts import render
from .models import Product
from django.db.models import Q


# Q함수를 통해 상품의 이름이나 설명을 OR이나 AND 조건으로 데이터 검색 가능


def home(request):
    return render(request, 'home.html')


def recommend1(request):
    return render(request, 'recommend1.html')


def recommend2(request):
    return render(request, 'recommend2.html')


def searchresult(request):
    if 'keyword' in request.GET:
        query = request.GET.get('keyword')
        # GET방식으로 받은 KEYWORD를 QUERY라고 칭함

        products = Product.objects.all().filter(
            Q(name__icontains=query) |
            Q(describtion__icontains=query) |
            Q(cafe_icontains=query)
        )
        # PRODUCT에서 filter를 통해 검사
        # __icontains로 name 안에 query와 동일한 값이 있는지 대소문자 상관없이 검색

    return render(request, 'recommend2.html', {'query': query, 'products': products})
    # 검색결과로 query랑 products 리턴


def filterresearch(request):
    if 'cafelist' and 'drinklist' in request.GET:
        cafe_list = request.GET.getlist('cafelist[]')
        drink_list = request.GET.getlist('drinklist[]')

        products = Product.objects.all().filter(
            Q(cafe__icontains=cafe_list) &
            Q(name_icontains=drink_list)
        )

    return render(request, 'recommend2.html', {'products': products})