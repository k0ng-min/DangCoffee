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


def search(request):
    if request.method == "POST":
        product = Product()
        if product.is_valid():
            product.cafe = request.POST.getlist('cafe', None)
            product.category = request.POST.getlist('drink', None)
            product.image = request.FILES['image']
            query = product.cafe and product.category
            if product:
                products = Product.objects.all().filter(
                    Q(cafe=product.cafe) &
                    Q(category=product.category)
                )

    else:
        query = request.GET.get('keyword')

        products = Product.objects.all().filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(cafe__icontains=query)
        )
    return render(request, 'recommend/recommend2.html', {'query': query, 'products': products})


def input_test(request):
    if request.POST:
        list_item = request.POST.getlist('test')
        print(list_item)

