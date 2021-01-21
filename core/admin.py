from django.contrib import admin
from .models import Product, ProductCategory, ProductAdditionalImage, ProductStock


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


@admin.register(ProductStock)
class ProductStockAdmin(admin.ModelAdmin):
    list_display = (
        "size_code",
        "size_name",
        "quantity",
        "color_name",
        "color_hex",
        "product",
    )
