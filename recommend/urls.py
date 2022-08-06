from django.urls import path
from . import views


app_name='recommend'

urlpatterns = [
    path('', views.searchresult, name="searchresult"),
    path('', views.filterresearch, name="filterresearch"),
]



