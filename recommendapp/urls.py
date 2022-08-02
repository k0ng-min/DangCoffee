from django.urls import path

from recommendapp.views import Suggest

app_name = "recommendappp"

urlpatterns = [
    path('Suggest/', Suggest, name='Suggest')
]