from django.urls import path

from core.views import products, home, product_details

urlpatterns = [
    path("products", products, name="products"),
    path("", home, name="home"),
    path("products/<int:id>", product_details, name="product_details"),
]
