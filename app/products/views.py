from rest_framework import viewsets

from .models import Product
from .serializers import ProductListSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    http_method_names = ['get', 'put', 'post']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductSerializer
        return self.serializer_class
