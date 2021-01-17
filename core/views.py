from django.shortcuts import render

from core.models import Product


def products(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, "products.html", context)


def product_details(request, id):
    context = {
        "product": Product.objects.get(id=id),
    }
    return render(request, "product_details.html", context)


def home(request):
    first_three_products = Product.objects.all()[:3]
    context = {
        "products": first_three_products,
    }
    return render(request, "home.html", context)
