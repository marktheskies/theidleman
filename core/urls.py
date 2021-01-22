from django.urls import path

from core.views import products, home, product_details, add_to_cart

urlpatterns = [
    path("products", products, name="products"),
    path("", home, name="home"),
    path("products/<int:id>", product_details, name="product_details"),
    path("add-to-cart/", add_to_cart, name="add_to_cart"),
]
