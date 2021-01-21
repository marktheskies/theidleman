from django.contrib import admin
from .models import Product, ProductCategory, ProductAdditionalImage, ProductStock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
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
    pass
