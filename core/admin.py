from django.contrib import admin

from .models import (
    Color,
    Product,
    ProductAdditionalImage,
    ProductCategory,
    Size,
)
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProductResource(resources.ModelResource):

    class Meta:
        model = Product

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "price",
        "discount_price",
        "category",
        "image",
    )
    resource_class = ProductResource


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


