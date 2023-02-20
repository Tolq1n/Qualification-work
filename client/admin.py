from django.contrib import admin

from .models import Client, Region, District


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region', 'district', 'address', 'contact')
    list_display_links  = ('id', 'name', 'region', 'district', 'address', 'contact')

admin.site.register(Region)
admin.site.register(District) 


