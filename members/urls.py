from django.urls import path
from members.views import signup, login, logout_view, profile, wishlist, add_to_wishlist, remove_wishlist_item

urlpatterns = [
    path('signup', signup, name='member_signup'),
    path('login', login, name='member_login'),
    path('logout', logout_view, name='member_logout'),
    path('profile', profile, name='member_profile'),
    path("wishlist/", wishlist, name="wishlist"),
    path("add-to-wishlist/", add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/remove-item/<wishlist_item_id>",
         remove_wishlist_item, name="remove_wishlist_item"),
]
