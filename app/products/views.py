from rest_framework import viewsets

from .models import (Category, Brand, Product, ProductDetail,
                     ProductImage, Review, Rating, SaveProduct, OrderProduct)
from .serializers import (ProductListSerializer, ProductSerializer, CategorySerializer, BrandSerializer, ReviewSerializer,
                          RatingSerializer, ProductDetailSerializer, ProductImageSerializer, SaveProductSerializer, OrderProductSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post']


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    http_method_names = ['get', 'post']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post']


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    http_method_names = ['get', 'post']


class SaveProductViewSet(viewsets.ModelViewSet):
    queryset = SaveProduct.objects.all()
    serializer_class = SaveProductSerializer
    http_method_names = ['get', 'post']


class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    http_method_names = ['get', 'post']


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    http_method_names = ['get', 'post']


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    http_method_names = ['get', 'post', 'put']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    http_method_names = ['get', 'put', 'post']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductSerializer
        return self.serializer_class
