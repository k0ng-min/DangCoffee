from django.urls import path

from . import views

app_name = 'beverage'
urlpatterns = [
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.product_delete, name='delete'),
    path('<int:pk>/update/',views.ProductUpdateView.as_view(), name = 'update'),
]