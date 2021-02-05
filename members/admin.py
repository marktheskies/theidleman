from django.contrib import admin

from .models import Member, CartItem


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass
