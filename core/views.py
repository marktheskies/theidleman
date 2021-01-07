from django.shortcuts import render

from core.models import Product


def products(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, "products.html", context)
