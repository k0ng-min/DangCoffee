from django.shortcuts import render
from .models import Product
from django.db.models import Q


# Q함수를 통해 상품의 이름이나 설명을 OR이나 AND 조건으로 데이터 검색 가능


def home(request):
    return render(request, 'home.html') # 변경


def recommend1(request):
    return render(request, 'recommend/recommend1.html')


def recommend2(request):
    return render(request, 'recommend/recommend2.html')


def search(request):
    if request.method == "POST":

        cafe = request.POST.getlist('cafe')
        category = request.POST.getlist('category')
        maxvalue = request.GET.get('priceRangeMax')
        minvalue = request.GET.get('priceRangeMin')
        query = "Tag List"

        q = Q()
        if cafe:
            q &= Q(cafe__icontain=cafe)
        if category:
            q &= Q(category__icontain=category)
        if maxvalue and minvalue:
            q &= Product.objects.filter(price__range=[minvalue, maxvalue])

        q &= Q(price__range=(minvalue, maxvalue))

        products = Product.objects.filter(q)

    else:

        query = request.GET.get('keyword')

        j = Q()
        if query:
            j |= Q(name__icontains=query)
            j |= Q(description__icontains=query)
            j |= Q(cafe__icontains=query)
        products = Product.objects.filter(j)

    return render(request, 'recommend/recommend2.html', {'query': query, 'products': products})

def input_test(request):
    if request.POST:
        list_item = request.POST.getlist('test')
        print(list_item)
