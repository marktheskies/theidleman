from random import randint, uniform, choices

from django.core.management import BaseCommand
from django.db import transaction
from core.factories import ProductFactory, ProductCategoryFactory
from core.models import Product, ProductCategory, ProductStock

NUM_PRODUCT_CATEGORIES = 10
NUM_PRODUCTS_PER_CATEGORY = 50
NUM_PRODUCT_VARIANCE = 40


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Deleting data...")

        models = [Product, ProductCategory, ProductStock]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating test data...")

        # Create product categories
        product_categories = []
        for _ in range(NUM_PRODUCT_CATEGORIES):
            product_category = ProductCategoryFactory()
            product_categories.append(product_category)

        # Create products
        for category in product_categories:
            minimum_products = NUM_PRODUCTS_PER_CATEGORY - NUM_PRODUCT_VARIANCE
            maximum_products = NUM_PRODUCTS_PER_CATEGORY + NUM_PRODUCT_VARIANCE
            num_products = randint(minimum_products, maximum_products)
            for _ in range(num_products):
                price = round(uniform(20, 100), 2)
                discount_price = choices([None, round(uniform(1, 20), 2)], [10, 2])[0]
                category = category
                product = ProductFactory(price=price, discount_price=discount_price, category=category)
