from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'contact', 'position', 'password')
    list_display_links = ('id', 'username', 'contact', 'position', 'password')

