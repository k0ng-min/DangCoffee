from django.urls import path
from . import views
from .views import CategoryView, MenuView, ProductView

app_name='infoapp'

urlpatterns = [
    path('/menu', MenuView.as_view()),
    path('/category', CategoryView.as_view()),
    path('/product', ProductView.as_view()),
]
