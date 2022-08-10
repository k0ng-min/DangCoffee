from django.urls import path
from . import views


app_name = 'recommend'

urlpatterns = [
    path('', views.searchresult, name="search"),
    path('', views.filterresearch, name="filterresearch"),
]



