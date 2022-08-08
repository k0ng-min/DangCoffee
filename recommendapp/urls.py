from django.urls import path

from recommendapp.views import Suggest

app_name = "recommendapp"

urlpatterns = [
    path('Suggest/', Suggest, name='Suggest')
]