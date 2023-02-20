from django.contrib import admin
from .models import Product, ManufacturedProduct, Category


admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'category']
    list_display_links = ['id', 'name', 'category']

@admin.register(ManufacturedProduct)
class ManufacturedProductAdmin(admin.ModelAdmin):
    list_display = ['id','product', 'amount',   'measure', 'unit_price', 'code', 'description', 'manufacture_date', 'active']
    list_display_links = ['id','product', 'amount',  'measure', 'unit_price', 'code', 'description', 'manufacture_date', 'active']
