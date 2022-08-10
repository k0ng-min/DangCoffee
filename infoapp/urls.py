from django.urls import path
from .views import MainSearch

app_name='info'

urlpatterns = [
    path('infolist/', MainSearch, name='infoapp'),
]
