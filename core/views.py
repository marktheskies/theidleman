from django.shortcuts import render, redirect
import json

from core.models import Product


def products(request):
    context = {"products": Product.objects.all()}
    return render(request, "products.html", context)


def product_details(request, id):
    context = {
        "product": Product.objects.get(id=id),
        "first_three_additional_images": Product.objects.get(
            id=id
        ).productadditionalimage_set.all()[:3],
    }
    return render(request, "product_details.html", context)


def home(request):
    first_three_products = Product.objects.all()[:3]
    context = {
        "products": first_three_products,
    }
    return render(request, "home.html", context)


def add_to_cart(request):
    if "cart" not in request.session:
        cart = []
    else:
        cart = request.session["cart"]

    cart.append({
        "product_id": request.POST["product_id"],
        "color": request.POST["color"],
        "size": request.POST["size"],
        "quantity": request.POST["quantity"],
    })

    request.session["cart"] = cart

    return redirect("/products")
