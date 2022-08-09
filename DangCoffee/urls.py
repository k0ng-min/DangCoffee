from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from recommend import views # views 이름 겹치는 것 수정!!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('recommend1/', views.recommend1),
    path('recommend2/', include('recommend.urls')),
    path('accounts/', include('accounts.urls'))
]
