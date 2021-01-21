from django.db import models


class ProductCategory(models.Model):
    """A category for products, such as Hoodies, Trousers, etc."""

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
        ProductCategory, models.SET_NULL, blank=True, null=True
    )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductStock(models.Model):
    """A size and availability of a product"""

    size_code = models.CharField(max_length=255)
    size_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, models.CASCADE)
