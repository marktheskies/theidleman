import uuid

from django.core.exceptions import FieldError
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.core.paginator import Paginator

from django.views.generic import TemplateView

import uuid

from core.models import Product, Color, Size
from members.models import CartItem

from blog.models import Post
from core.models import Product, ProductCategory


def products(request, category=None):
    """Renders the products page"""
    if category:
        products_result = Product.objects.filter(category__name=category)

        product_paginator = Paginator(products_result, 8)

        page_num = request.GET.get("page")

        page = product_paginator.get_page(page_num)

        context = {
            "category": category,
            "count": product_paginator.count,
            "page": page
        }
    else:
        products_result = Product.objects.all()

        product_paginator = Paginator(products_result, 8)

        page_num = request.GET.get("page")

        page = product_paginator.get_page(page_num)

        context = {
            "count": product_paginator.count,
            "page": page
        }

    # Product sorting
    if request.GET.get("sort"):
        try:
            context["products"]: context["products"].order_by(
                request.GET.get("sort"))
        except FieldError:
            # The give field does not exist on the Product, thus we must skip sorting.
            pass

    return TemplateResponse(request, "products.html", context) 


def product_details(request, id):
    context = {
        "product": Product.objects.get(id=id),
        "first_three_additional_images": Product.objects.get(
            id=id
        ).productadditionalimage_set.all()[:3],
    }
    return TemplateResponse(request, "product_details.html", context)


def home(request):
    first_three_products = Product.objects.all()[:3]
    context = {
        "products": first_three_products,
        "post_list": Post.objects.all()[:3]
    }
    return TemplateResponse(request, "home.html", context)


def add_to_cart(request):
    if "cart" not in request.session:
        cart = []
    else:
        cart = request.session["cart"]

    session_item_id = str(uuid.uuid4())

    if request.user.is_authenticated:
        ci = CartItem(
            member_id=request.user.member.id,
            item_id=request.POST["product_id"],
            session_item_id=session_item_id,
            quantity=request.POST["quantity"]
        )
        ci.color = Color.objects.get(hex_value=request.POST["color"])
        ci.size = Size.objects.get(name=request.POST["size"])
        ci.save()

    cart.append({
        "session_item_id": session_item_id,
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

    request.user.member.cartitem_set.all().delete()

    # Redirect to the last page (HTTP_REFERRER). If HTTP_REFERER is empty, for example, if the user hits "back",
    # or navigates to the page directly, redirect to the homepage.
    return redirect(request.META.get("HTTP_REFERER", '/'))


def cart_context(request):
    """Creates a context suitable for cart and checkout pages, containing products, subtotal, 
    shipping and total."""
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
                "session_item_id": item["session_item_id"],
                "product": product,
                "quantity": item["quantity"],
                "total": item_total_cost,
                "color": item["color"],
                "size": item["size"],
            })
            context["subtotal"] += item_total_cost
            if not product.free_delivery:
                context["free_delivery"] = False

        if context["subtotal"] > 100:
            context["free_delivery"] = True

        if context["free_delivery"]:
            context["total"] = context["subtotal"]
        else:
            context["total"] = context["subtotal"] + 15

    return context


def remove_shopping_cart_item(request, session_item_id):
    """Removes an item from the session shopping cart, by its unique ID in the session."""

    # Remove the item from member db cart storage if the user is authenticated.
    if request.user.is_authenticated:
        request.user.member.cartitem_set.filter(
            session_item_id=session_item_id).delete()

    # If the cart is empty, just redirect to the home page.
    if "cart" not in request.session:
        return redirect("/")

    new_items = []
    for item in request.session["cart"]:
        if item["session_item_id"] != session_item_id:
            new_items.append(item)

    request.session["cart"] = new_items

    return redirect("/shopping-cart")


def shopping_cart(request):
    context = cart_context(request)
    return TemplateResponse(request, "shopping_cart.html", context)


def checkout(request):
    context = cart_context(request)
    return render(request, "checkout.html", context)

  
class InstagramFeed(TemplateView):
    template_name = 'instagram_feed.html'
  
  
def instagram_feed(request):
    return render(request, "instagram_feed.html")

  
def contact(request):
    return render(request, "contact.html")
