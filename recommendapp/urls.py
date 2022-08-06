from django.urls import path

from recommendapp.views import ReDetailView, ReListView

app_name = "recommendappp"

urlpatterns = [
    path('list/', ReListView.as_view(), name='list'),
    path('detail/<int:pk>', ReDetailView.as_view(), name='detail'),
]