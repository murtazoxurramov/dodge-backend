from django.contrib import admin

from .models import Category, Brand, Product, ProductDetail, ProductImage, Review, Rating


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(Rating)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductDetailAdmin(admin.StackedInline):
    model = ProductDetail


@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines = [ProductImageAdmin, ProductDetailAdmin]

    class Meta:
        model = Product
