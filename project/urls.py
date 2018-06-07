"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ads.api import AdListAPI, AdDetailAPI, MyAdsAPI
from ads.views import HomeView, AdDetailView, AdFormView, MyAdsView
from users.api import UsersAPI, UserDetailAPI
from users.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('mis-anuncios', MyAdsView.as_view(), name='my-ads'),
    path('anuncio/nuevo', AdFormView.as_view(), name='ad-form'),
    path('anuncio/<int:pk>', AdDetailView.as_view(), name='ad-detail'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    # API URLs
    path('api/v1/users/', UsersAPI.as_view(), name='api-users'),
    path('api/v1/users/<int:pk>/', UserDetailAPI.as_view(), name='api-user-detail'),

    path('api/v1/ads/', AdListAPI.as_view(), name='api-ads'),
    path('api/v1/ads/<int:pk>/', AdDetailAPI.as_view(), name='api-ads-detail'),
    path('api/v1/ads/mine/', MyAdsAPI.as_view(), name='api-ads-mine')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
