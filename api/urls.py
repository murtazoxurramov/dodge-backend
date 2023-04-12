from rest_framework import routers
from django.urls import path, include

from app.products.views import ProductViewSet

router = routers.DefaultRouter()

router.register(r'product', ProductViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls))
]
