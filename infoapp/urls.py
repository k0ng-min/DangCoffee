from django.urls import path
from . import views


app_name='infoapp'

urlpatterns = [
    path('', views.productlist, name='infolist'),
    path('info/result/', views.productresult, name='result')
]
