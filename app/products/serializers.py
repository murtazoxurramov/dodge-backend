import statistics
from rest_framework import serializers

from .models import (Category, Brand, Product, ProductDetail,
                     ProductImage, Review, Rating, SaveProduct, OrderProduct)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'default_attributes']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'logo']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['stars']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'text']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['attribute', 'value', 'is_main']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'is_main']


class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'price', 'rating', 'image']

    def get_image(self, obj):
        image = ProductImage.objects.filter(
            product=obj, is_main=True).prefetch_related('product')
        return ProductImageSerializer(image, many=True).data

    def get_rating(self, obj):
        data = Rating.objects.filter(
            product=obj).all().prefetch_related('product')
        stars = []
        for item in data:
            stars.append(item.stars)
        mean = statistics.mean(stars)
        approx_mean = int(round(mean, 0))
        return approx_mean


class ProductSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'category', 'price',
                  'details', 'images', 'rating', 'reviews']

    def get_details(self, obj):
        details = ProductDetail.objects.filter(
            product=obj).prefetch_related('product')
        return ProductDetailSerializer(details, many=True).data

    def get_images(self, obj):
        images = ProductImage.objects.filter(
            product=obj).prefetch_related('product')
        return ProductImageSerializer(images, many=True).data

    def get_rating(self, obj):
        data = Rating.objects.filter(
            product=obj).all().prefetch_related('product')
        stars = []
        for item in data:
            stars.append(item.stars)
        mean = statistics.mean(stars)
        approx_mean = int(round(mean, 0))
        return approx_mean

    def get_reviews(self, obj):
        reviews = Review.objects.filter(product=obj)
        return ReviewSerializer(reviews, many=True).data


class SaveProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveProduct
        fields = ['id', 'user', 'product']


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['id', 'user', 'product']
