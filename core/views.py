from django.shortcuts import render, redirect

from core.models import Product, Color, Size
from members.models import CartItem

import uuid


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

    # Remove the item from member db cart storage.
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
    return render(request, "shopping_cart.html", context)


def checkout(request):
    context = cart_context(request)
    return render(request, "checkout.html", context)


from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm


def contact(request):
        form_class = ContactForm
        form = form_class(request.POST or None)
        if request.method == 'POST':

            if form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                number = request.POST.get('number')
                message = request.POST.get('message')

                send_mail('Subject here', message, email, ['testmail@gmail.com'], fail_silently=False) 
                return HttpResponseRedirect('/contact')
    
        return render(request, "contact.html", {'form': form})

