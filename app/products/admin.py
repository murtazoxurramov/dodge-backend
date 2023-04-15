from django.contrib import admin

from .models import (Category, Brand, Product, ProductDetail,
                     ProductImage, Review, Rating, SaveProduct, OrderProduct)


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(SaveProduct)
admin.site.register(OrderProduct)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductDetailAdmin(admin.StackedInline):
    model = ProductDetail


@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines = [ProductImageAdmin, ProductDetailAdmin]

    class Meta:
        model = Product
