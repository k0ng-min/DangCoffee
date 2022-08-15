from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from . import views
from recommend import views as recommend_views
from accounts import views as accounts_views
from mypage import views as mypage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', recommend_views.home, name='home'), # ' '로 변경!

    path('recommend1/', recommend_views.recommend1),
    path('recommend2/', include('recommend.urls')),

    path('accounts/', include('accounts.urls')),
    path('social_accounts/', include('allauth.urls')),

    path('mypage/', mypage_views.first, name='mypage'),

]
