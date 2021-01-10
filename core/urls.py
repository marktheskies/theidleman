from django.urls import path

from core.views import products, home

urlpatterns = [
    path('products', products, name='products'),
    path('', home, name='home'),
]
