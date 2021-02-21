from django.urls import path

from core.views import (products, home, product_details, add_to_cart, empty_cart, shopping_cart,
                        checkout, remove_shopping_cart_item, social_media_feed, contact, search_results)

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
    path("social-media-feed/", social_media_feed, name="social_media_feed"),
    path("contact/", contact, name="contact"),
    path("shopping-cart/remove-item/<session_item_id>",
         remove_shopping_cart_item, name="remove_shopping_cart_item"),
    path("search-results/", search_results, name="search_results"),
]
