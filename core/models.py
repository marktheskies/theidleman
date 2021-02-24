"""Contains all E-Commerce related models for The Idle Man"""

from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ProductCategory(models.Model):
    """A category for products, such as Hoodies, Trousers, etc."""

    class Meta:
        verbose_name_plural = "product categories"

    name = models.CharField(max_length=255, unique=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Color(models.Model):
    """A color for a product"""

    hex_value = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.hex_value


class Size(models.Model):
    """A size for a product"""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """A product to sell"""

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(
        ProductCategory, models.SET_NULL, blank=True, null=True, related_name='products'
    )

    # The main image of the product
    image = CloudinaryField('image', null=True)
    image_reference = models.TextField(blank=True)

    free_delivery = models.BooleanField(default=False)

    # Rating is static, for now. TODO: Extend the rating to allow actual user reviews.
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)],
        default=0,
    )

    care_instructions = models.TextField(null=True, blank=True)

    sizes = models.ManyToManyField(Size)
    colors = models.ManyToManyField(Color)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_related_products(self):
        return Product.objects.filter(category=self.category)


class ProductAdditionalImage(models.Model):
    """An additional image of a product"""

    image = CloudinaryField('image', null=True)
    reference = models.TextField(blank=True)
    product = models.ForeignKey(Product, models.CASCADE)
