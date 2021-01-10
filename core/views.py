from django.shortcuts import render

from core.models import Product


def products(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, "products.html", context)


def home(request):
    first_three_products = Product.objects.all()[:3]
    context = {
        "products": first_three_products,
    }
    return render(request, "home.html", context)
