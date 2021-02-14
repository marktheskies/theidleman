from django.urls import path

from core.views import products, home, product_details, add_to_cart, empty_cart, shopping_cart, checkout, remove_shopping_cart_item, contact, wishlist, add_to_wishlist, remove_wishlist_item

urlpatterns = [
    path("products/", products, name="products"),
    path("products/categories/<str:category>/",
         products, name="products_with_category"),
    path("", home, name="home"),
    path("products/<int:id>", product_details, name="product_details"),
    path("add-to-cart/", add_to_cart, name="add_to_cart"),
    path("empty-cart/", empty_cart, name="empty_cart"),
    path("shopping-cart/", shopping_cart, name="shopping_cart"),
    path("checkout/", checkout, name="checkout"),
    path("contact/", contact, name="contact"),
    path("shopping-cart/remove-item/<session_item_id>",
         remove_shopping_cart_item, name="remove_shopping_cart_item"),
    path("wishlist/", wishlist, name="wishlist"),
    path("add-to-wishlist/", add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/remove-item/<session_item_id>",
         remove_wishlist_item, name="remove_wishlist_item"),
]
