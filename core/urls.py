from django.urls import path

from core.views import products

urlpatterns = [
    path('products', products, name='products')
]