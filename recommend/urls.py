from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


app_name = 'recommend'

urlpatterns = [
    path('', views.search, name="search"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
