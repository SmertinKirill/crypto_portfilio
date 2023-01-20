from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import BuyViewSet, PortfolioViewSet, SellViewSet

router = routers.DefaultRouter()
router.register(r'portfolio', PortfolioViewSet, basename='portfolio')
router.register(r'buy', BuyViewSet, basename='buy')
router.register(r'sell', SellViewSet, basename='sell')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
