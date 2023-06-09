from django.utils import timezone
from django.db import models
from django.db.models import Avg
from django.conf import settings

from app.users.models import User


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('product_set')


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    default_attributes = models.JSONField(blank=True)
    icon = models.FileField(upload_to='uploads/category/icons/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    @property
    def icon_url(self):
        if self.icon:
            return "%s%s" % (settings.HOST, self.icon.url)


class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.FileField(upload_to='uploads/brand/logos/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def logo_url(self):
        if self.logo:
            return "%s%s" % (settings.HOST, self.logo.url)


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.pk:  # if the product is being created
    #         # create default product details based on category default attributes
    #         for attribute, value in self.category.default_attributes.items():
    #             ProductDetail.objects.create(
    #                 product=self, attribute=attribute, value=value)
    #     super().save(*args, **kwargs)

    def rating(self):
        return Rating.objects.filter(product=self).aggregate(Avg('stars'))['stars__avg']


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    is_main = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.title} - {self.attribute}: {self.value}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to='uploads/products/images/')
    is_main = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)


class SaveProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Saved Product'
        verbose_name_plural = 'Saved Products'
        unique_together = ['user', 'product']

    def __str__(self):
        return f"{self.user.username} saved {self.product.title}"


class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Ordered Product'
        verbose_name_plural = 'Ordered Products'

    def __str__(self):
        return f"{self.user.username} ordered {self.product.title}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s review for {self.product.title} ({self.created_at})"


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.stars} stars for {self.product.title}"
