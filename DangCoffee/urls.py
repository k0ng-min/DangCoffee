from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from recommend import views as recommend_views
# from accounts import views as accounts_views
# from mypage import views as mypage_views
import infoapp.views
from recommend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # 네임스페이스('home') 추가 (22.08.17)

    # part 1 : 로그인, 마이페이지
    path('accounts/', include('accounts.urls')),
    path('social_accounts/', include('allauth.urls')),
    path('mypage/', include('mypage.urls')),

    # part 2 : 정보
    path('info/', infoapp.views.productlist),
    path('info/', include('infoapp.urls')),

    # part 3 : 추천
    path('recommend1/', recommend_views.recommend1),
    path('recommend2/', include('recommend.urls')),

]
