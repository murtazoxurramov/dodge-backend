from rest_framework import routers
from django.urls import path, include

from app.products.views import (ProductViewSet, BrandViewSet, CategoryViewSet, RatingViewSet, ReviewViewSet,
                                ProductDetailViewSet, ProductImageViewSet, SaveProductViewSet, OrderProductViewSet)

router = routers.DefaultRouter()

router.register(r'product', ProductViewSet, basename='products')
router.register(r'category', CategoryViewSet, basename='categories')
router.register(r'brand', BrandViewSet, basename='brands')
router.register(r'rating', RatingViewSet, basename='ratings')
router.register(r'review', ReviewViewSet, basename='reviews')
router.register(r'product-detail', ProductDetailViewSet, basename='product-details')
router.register(r'product-image', ProductImageViewSet, basename='product-images')
router.register(r'save-product', SaveProductViewSet, basename='save-products')
router.register(r'order-product', OrderProductViewSet, basename='order-products')


urlpatterns = [
    path('', include(router.urls))
]
