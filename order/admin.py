from django.contrib import admin
from .models import  Order
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'employee', 'product', 'payment_type']
    list_display_links = ['client', 'employee', 'product', 'payment_type']


# admin.site.register(Order)



