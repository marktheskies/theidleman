from django.test import TestCase
from .models import ProductCategory, Product

class ProductsTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="The Idle Man Signature Hoodie", description="This is the test description for the Idle Man Signature Hoodie")
