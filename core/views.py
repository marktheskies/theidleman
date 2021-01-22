from django.shortcuts import render, redirect

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


def empty_cart(request):
    """Removes all items in cart. If the cart session variable does not exist, does nothing."""
    if "cart" in request.session:
        request.session["cart"] = []

    # Redirect to the last page (HTTP_REFERRER). If HTTP_REFERER is empty, for example, if the user hits "back",
    # or navigates to the page directly, redirect to the homepage.
    return redirect(request.META.get("HTTP_REFERER", '/'))


def shopping_cart(request):
    context = {
        "items": [],
        "subtotal": 0.0,
        "free_delivery": True,
        "total": 0
    }
    if "cart" in request.session:
        for item in request.session["cart"]:
            product = Product.objects.get(id=item["product_id"])
            item_total_cost = product.price * float(item["quantity"])
            context["items"].append({
                "product": product,
                "quantity": item["quantity"],
                "total": item_total_cost,
                "color": item["color"],
                "size": item["size"],
            })
            context["subtotal"] += item_total_cost
            if not product.free_delivery:
                context["free_delivery"] = False

        if context["free_delivery"]:
            context["total"] = context["subtotal"]
        else:
            context["total"] = context["subtotal"] + 15

    return render(request, "shopping_cart.html", context)
