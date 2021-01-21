from django.contrib import admin

from .models import (
    Color,
    Product,
    ProductAdditionalImage,
    ProductCategory,
    Size,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "price",
        "discount_price",
        "category",
        "image",
    )


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAdditionalImage)
class ProductAdditionalImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass
