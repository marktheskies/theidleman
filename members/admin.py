from django.contrib import admin

from .models import Member, CartItem, WishlistItem


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    pass
