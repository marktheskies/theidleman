import factory
from factory.django import DjangoModelFactory, ImageField
from random import uniform, choices

from .models import Product, ProductCategory


class ProductCategoryFactory(DjangoModelFactory):
    class Meta:
        model = ProductCategory

    name = factory.Faker("sentence", nb_words=1)


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("paragraph")
    image = ImageField()
