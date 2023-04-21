from rest_framework import routers
from django.urls import path, include

from app.products.views import (ProductViewSet, BrandViewSet, CategoryViewSet, RatingViewSet, ReviewViewSet,
                                ProductDetailViewSet, ProductImageViewSet, SaveProductViewSet, OrderProductViewSet)
from app.users.views import UserLoginView, UserRegistrationView, UserLogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()

router.register(r'product', ProductViewSet, basename='products')
router.register(r'category', CategoryViewSet, basename='categories')
router.register(r'brand', BrandViewSet, basename='brands')
router.register(r'rating', RatingViewSet, basename='ratings')
router.register(r'review', ReviewViewSet, basename='reviews')
router.register(r'product-detail', ProductDetailViewSet,
                basename='product-details')
router.register(r'product-image', ProductImageViewSet,
                basename='product-images')
router.register(r'save-product', SaveProductViewSet, basename='save-products')
router.register(r'order-product', OrderProductViewSet,
                basename='order-products')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('signin/', UserSignInView.as_view(), name='user_signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
