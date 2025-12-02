from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'fabric', 'color', 'price', 'in_stock')
    list_filter = ('category', 'fabric', 'in_stock')
    search_fields = ('name', 'color')

admin.site.register(Product, ProductAdmin)

